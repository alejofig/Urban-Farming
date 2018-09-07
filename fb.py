# coding=utf-8
import pyrebase                             #Libreria firebase
import serial                                   #Libreria puerto serial
from time import sleep                   #Librería delay

arduino = serial.Serial('/dev/ttyUSB0', 9600)  #Declara puerto serial arduino

config = {                  #Configuración firebase
  "apiKey": "AIzaSyD4rXiUJKaVBNDIniybQJvMg-_tZLY9jMw",
  "authDomain": "solo-farm.firebaseapp.com",
  "databaseURL": "https://solo-farm.firebaseio.com",
  "storageBucket": "solo-farm.appspot.com"
}

firebase = pyrebase.initialize_app(config) #Inicializa objeto firebase

db = firebase.database()         #Relaciona la base de datos
def convert(value):                 #Función para convertir entrada bool de la base de datos
    if value == True:                 # en un caracter para enviar por puerto serial
        state='H'
    else:
        state='L'
    return state
read=' '
data =' '
print "**********   INICIO  *************"
salidaLed1_ant=db.child("home/led1").get()   #Obtiene el estado del checkbox
salidaLed2_ant=db.child("home/led2").get()
salidaLed3_ant=db.child("home/led3").get()
#print "Led", salidaLed1_ant.val()                      #Imprime el valor  booleano T/F
while True:                                                        #Bucle infinito
    salidaLed1 = db.child("home/led1").get()    #Obtiene el estado del checkbox
    salidaLed2 = db.child("home/led2").get()
    salidaLed3 = db.child("home/led3").get()

    if salidaLed1.val() != salidaLed1_ant.val():
        print "Led H", salidaLed1.val()                       #Imprime el estado del checkbox
        salidaLed1_ant=salidaLed1                         #Actualiza el estado anterior
        data=convert(salidaLed1.val())                     #Envía el dato obtenido para convertir
        arduino.flush()
        sleep(0.1)
        arduino.write(data)                                       #Escribe al puerto serial el valor convertido H o L
        sleep(0.1)
        while arduino.inWaiting()>0:
            read+=arduino.read(1)
        print "arduino", read
        read=' '

    elif salidaLed2.val() != salidaLed2_ant.val():
        print "Led L", salidaLed2.val()                       #Imprime el estado del checkbox
        salidaLed2_ant=salidaLed2                         #Actualiza el estado anterior
        data ='3'
        arduino.flush()
        sleep(0.1)
        arduino.write(data)
        sleep(0.1)
        while arduino.inWaiting()>0:
            read+=arduino.read(1)
        print "arduino", read
        read=' '

    elif  salidaLed3.val() != salidaLed3_ant.val():
        print "Led 3", salidaLed3.val()                       #Imprime el estado del checkbox
        salidaLed3_ant=salidaLed3                         #Actualiza el estado anterior
        data ='3'
        arduino.flush()
        sleep(0.1)
        arduino.write(data)
        sleep(0.1)
        while arduino.inWaiting()>0:
            read+=arduino.read(1)
        print "arduino", read
        read=' '
arduino.close()                                                    #Cierra el puerto
