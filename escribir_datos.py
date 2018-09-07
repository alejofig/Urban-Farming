# coding=utf-8
                          #Libreria puerto serial
from time import sleep                   #Librer�a delay
from datetime import datetime, date, time, timedelta #Librer�a fechas

import pyrebase

config = {                  #Configuraci�n firebase
  "apiKey": "AIzaSyD4rXiUJKaVBNDIniybQJvMg-_tZLY9jMw",
  "authDomain": "solo-farm.firebaseapp.com",
  "databaseURL": "https://solo-farm.firebaseio.com",
  "storageBucket": "solo-farm.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()                #Relaciona la base de datos a una variable

def escribir(dato,tipo):
    file=open("log.txt","a")
    if tipo==1:
        file.write(str(dato)+ ' ')
        file.close()
    elif tipo==2:
        file.write(dato+'\n')
        file.close()
#Funci�n para enviar datos a Firebase
def syncfb(ph,temp,hum,luz,ce,fecha):
        #Inicializa variables para los sensores
        # ph=0
        # temp=0
        # hum=0
        # light =0

        hoy = datetime(fecha.year, fecha.month, fecha.day, fecha.hour, fecha.minute, fecha.second) # Obtiene la fecha
        dia = date(fecha.year, fecha.month, fecha.day) #Extrae el d�a
        hora = time(fecha.hour, fecha.minute, fecha.second) #Extrae la Hora
        vector = [ph,temp,hum,luz,ce] #Vector con los datos
        # k=0
        # for i in vector:            #Ciclo for para asignar los datos a las variables de los sensores
        #     if  k == 0:
        #         ph=i
        #         #print i
        #     elif  k == 1:
        #         temp=i
        #         #print i
        #     elif  k == 2:
        #         hum=i
        #         #print i
        #     elif  k == 3:
        #         light=i
        #         #print i
        #     k+=1
        name="Sample "+ str(hoy)  #Define el nombre del keylog
        data = {"ph": ph,"temp": temp,"hum": hum,"light": luz, "ce": ce, "Day": str(dia), "Hour": str(hora)} #Datos a escribir
        db.child("user").child(name).set(data) #Escribe los datos en firebase




'''
# coding=utf-8
                          #Libreria puerto serial
from time import sleep                   #Librer�a delay
from datetime import datetime, date, time, timedelta #Librer�a fechas

import pyrebase

config = {                  #Configuraci�n firebase
  "apiKey": "AIzaSyD4rXiUJKaVBNDIniybQJvMg-_tZLY9jMw",
  "authDomain": "solo-farm.firebaseapp.com",
  "databaseURL": "https://solo-farm.firebaseio.com",
  "storageBucket": "solo-farm.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()                #Relaciona la base de datos a una variable

def escribir(dato,tipo):
    file=open("log.txt","a")
    if tipo==1:
        file.write(str(dato)+ ' ')
        file.close()
    elif tipo==2:
        file.write(dato+'\n')
        file.close()
#Funci�n para enviar datos a Firebase
def syncfb(ph,temp,hum,luz,ce,fecha):
        #Inicializa variables para los sensores
        # ph=0
        # temp=0
        # hum=0
        # light =0

        hoy = datetime(fecha.year, fecha.month, fecha.day, fecha.hour, fecha.minute, fecha.second) # Obtiene la fecha
        dia = date(fecha.year, fecha.month, fecha.day) #Extrae el d�a
        hora = time(fecha.hour, fecha.minute, fecha.second) #Extrae la Hora
        vector = [ph,temp,hum,luz] #Vector con los datos
        # k=0
        # for i in vector:            #Ciclo for para asignar los datos a las variables de los sensores
        #     if  k == 0:
        #         ph=i
        #         #print i
        #     elif  k == 1:
        #         temp=i
        #         #print i
        #     elif  k == 2:
        #         hum=i
        #         #print i
        #     elif  k == 3:
        #         light=i
        #         #print i
        #     k+=1
        name="Sample "+ str(hoy)  #Define el nombre del keylog
        data = {"ph": ph,"temp": temp,"hum": hum,"light": luz, "Day": str(dia), "Hour": str(hora), "ce": ce} #Datos a escribir
        db.child("user").child(name).set(data) #Escribe los datos en firebase
'''