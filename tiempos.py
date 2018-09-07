# coding=utf-8
import serial                            #Libreria puerto serial
from time import sleep                   #Librer�a delay
from datetime import datetime, date, time, timedelta #Librer�a fechas
# import numpy as np
import pyrebase                           #Libreria firebase
import collections
import escribir_datos
import detection
# Inicializaci�n
arduino = serial.Serial('/dev/ttyACM0', 9600)  #Declara puerto serial arduino
config = {                  #Configuraci�n firebase
  "apiKey": "AIzaSyD4rXiUJKaVBNDIniybQJvMg-_tZLY9jMw",
  "authDomain": "solo-farm.firebaseapp.com",
  "databaseURL": "https://solo-farm.firebaseio.com",
  "storageBucket": "solo-farm.appspot.com"
}
#Inicializa Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()                #Relaciona la base de datos a una variable

#Numero de variables
N=5
data=[0,0,0,0,0]          #Array para guardar los datos
cicle=False             #No toma en cuenta el primer ciclo
buffer=' '              #Variable para la lectura de los datos de Arduino
a= " "                  #Variable para guardar los datos a un txt
flag=False              #Boolean para el control del ciclo
ce=0


#Funci�n para escribir los datos en un txt
arduino.write('O') #Se asegura de apagar la bomba
arduino.write('L') #Se asegura de tener apagado el bombillo
arduino.write('C') #Se asegura de tener apagado el bombillo azul1
print  "          Urban Farmer           "  #Inicio
print  "**********   Start  *************"
while True:
    arduino.flush()         #Limpia el puerto serial
    timeN = datetime.now()  #Fecha y hora Actual
    timeN1 = time(timeN.hour,timeN.minute) #Extrae la hora
        #timeN1=time(14,16)

    if timeN1.hour==6 or timeN1.hour == 8 or timeN1.hour == 10 or timeN1.hour == 12 or timeN1.hour==14 or timeN1.hour == 16 or timeN1.hour == 18:
        if  timeN1.minute==00:            #inicio del riego
            arduino.write('H')           #apagar aireador
            arduino.write('R')           #apagar ventilador
            print "Start Irrigation"
            arduino.write('P')           #Encender bomba
            sleep(20)
            print "Stop Irrigation"     #fin del riego
            arduino.write('O')          #Apagar bomba
            sleep(40)

    if timeN1.hour==5 or timeN1.hour == 7 or timeN1.hour == 9 or timeN1.hour == 11 or timeN1.hour==13 or timeN1.hour == 15 or timeN1.hour == 17:
        if timeN1.minute == 50: #Enciende el aireador 10 min antes del riego
            print "Mix"                      #inicio de mezcla
            arduino.write('X')               #Encender aireador
            #arduino.write('E')              # Encender ventilador
            sleep(0.5)
            flag=True

    

    if timeN1.minute ==02:
        arduino.write('L')
        arduino.write('C')
        sleep(2)

    if timeN1.minute== 02 or timeN1.minute== 22 or timeN1.minute== 42:#Lectura de datos
        if cicle==True:

            print "Ready..."

            arduino.write('D')                #Tomar datos
            sleep(1)
            i=0
            while i<N:                         #Recibe 4 datos
                try:
                    while arduino.inWaiting()>0:  #Espera a que arduino env�e los datos
                        buffer=arduino.readline()   #Lee dato por dato
                        data[i]=float(buffer)       #Almacena
                        buffer=' '                  #Limpia variable de lectura
                        a=str(data[i])              #VAriable para escritura
                        escribir_datos.escribir(a,1)               #Invoca funci�n para escribir txt
                        a=" "                       #Limpia variable para escribir
                        if i <5:                    #Rompe el ciclo a las 4 muestras
                           i=i+1
                        else:
                            break
                    break
                except KeyboardInterrupt:           #Lectura de ctrl+c para detener
                    print ("Shutdown")
                    break
            #Se muestran los datos recogidos en la consola


            if (data[0]==0 or data[1]==0 or data[2]==0):
                i=0
                print "Error en lectura de datos"
                print "Date: ", timeN
                print "Reintentar"
            else:
                escribir_datos.syncfb(str(data[1]),str(data[2]),str(data[3]),str(data[4]),str(data[0]),timeN) #Invoca funci�n para enviar datos a firebase
                print "Data Sending"
                print "pH: ",data[0]
                print "Temperature: ",data[1]
                print "Humidity: ",data[2]
                print "Light: ",data[3]
                print "C.E: ",data[4]
                print "Date: ", timeN
                print "Data Sent"

                if data[4]>5000 and timeN1.minute == 02 :
                    if timeN1.hour >6 and timeN1.hour < 19:
                        print "Luz ambiente suficiente, apagando bombillo"
                        arduino.write('C')
                        arduino.write('L')

                elif data[4]<=5000 and timeN1.minute == 02:
                    if  timeN1.hour >6 and timeN1.hour < 19:
                        print "Luz activada"

                        arduino.write('Z')                #Activaci�n del bombillo morado
                        sleep(2)
                        arduino.write('B')                #Activaci�n del bombillo Azul1
                    else:
                        arduino.write('L')                #Apagar del bombillo
                        arduino.write('C')                #Apagar bombillo Azul1
                        print "Bombillo apagado, noche"

                #codigo para controlar ventilador
                if data[2]>=21:
                    print "Temperatura alta, encendiendo ventilador"
                   # arduino.write('E')      #Ventilador encendido
                else:
                    print "Temperatura normal"
                    #arduino.write('R')    # Ventilador apagado


                sleep(50)
                escribir_datos.escribir(str(timeN1),2)

            #escribir(str(timeN1.day),2)
             #Espera
             #Activaci�n de la luz dependiendo del sensor y las horas


            data=[0,0,0,0,0]
            i=0
    cicle=True

    sleep(1)
