"""


import cv2
import numpy as np
import time
import picamera



print ("Hola")
def detectar_lechuga():

    with picamera.PiCamera() as picam:
        picam.start_preview()
        time.sleep(5)
        picam.capture('lechugas.jpg')
        picam.stop_preview()
        picam.close()

    imagen = cv2.imread('calidad4.jpg')
    imagen2 = cv2.imread('calidad4.jpg')
    image = imagen
    img = cv2.imread('calidad4.jpg',0)


    height = imagen.shape[0]
    width = imagen.shape[1]
    channels = imagen.shape[2]



    # foto del raspberry
    #print(height)
    #print(width)
    #print(channels)
    fotoRaspberry = image.copy()
    cv2.imshow("FotoRaspberry", fotoRaspberry)
    #cv2.imwrite("imageLine.jpg", imageLine)

    #Suavizado de la imagen
    blur = cv2.blur(fotoRaspberry,(5,5))
    cv2.imshow("Suavizado", blur)
    #Convertir BGR2HSV
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)
    #DEfinicion de rangos
    verdes_bajos = np.array([30,50,50])
    verdes_altos = np.array([70,255,255])

    #aplicacion de la mascara

    mask = cv2.inRange(hsv,verdes_bajos,verdes_altos)
    cv2.imshow("mascara", mask)

    ret,thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)

    img2,contours,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    M = cv2.moments(cnt)

    area = cv2.contourArea(cnt)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    #print(cx)
    #print(cy)
    #print(area)

    ###
    for c in contours:
        area = cv2.contourArea(c)
        print("Area")
        print(area)
        if area > 1000 and area < 1000000:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)

    print("numero de contronos")
    print(len(contours))
    cv2.imshow("rectangulos", imagen)
    numero = 0
    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000 and area < 100000000:
            cv2.drawContours(imagen2, [c], 0, (0, 0, 255), 2, cv2.LINE_AA)
            numero = numero + 1
            print("El area de la lechuga es: " + str(area))

    print("El numero de lechugas es: " + str(numero))

    cv2.imshow("contornos", imagen2)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""


import cv2
import numpy as np
import time
import picamera

def detectar_lechuga():
    print ("Hola2")
    with picamera.PiCamera() as picam:
        picam.start_preview()
        time.sleep(5)
        picam.capture('lechugas.jpg')
        picam.stop_preview()
        picam.close()

        imagen = cv2.imread('lechugas.jpg')
        imagen2 = cv2.imread('lechugas.jpg')
        image = imagen
        img = cv2.imread('lechugas.jpg',0)


        height = imagen.shape[0]
        width = imagen.shape[1]
        channels = imagen.shape[2]



    # foto del raspberry
    print(height)
    print(width)
    print(channels)
    fotoRaspberry = image.copy()
#cv2.imshow("FotoRaspberry", fotoRaspberry)
#cv2.imwrite("imageLine.jpg", imageLine)

    #Suavizado de la imagen
    blur = cv2.blur(fotoRaspberry,(5,5))
#cv2.imshow("Suavizado", blur)
#Convertir BGR2HSV

    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV", hsv)
#DEfinicion de rangos
    verdes_bajos = np.array([30,50,50])
    verdes_altos = np.array([70,255,255])

    #aplicacion de la mascara

    mask = cv2.inRange(hsv,verdes_bajos,verdes_altos)
#cv2.imshow("mascara", mask)



    ret,thresh = cv2.threshold(mask,127,255,0)
    cv2.imwrite("thresh.jpg", mask)
    img2,contours,hier = cv2.findContours(thresh,1,2)


    cnt = contours[0]


    M = cv2.moments(cnt)
    print("Este es m", M )

    area = cv2.contourArea(cnt)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    #print(cx)
    #print(cy)
    #print(area)

    print("Esta es la area:", area)


    for c in contours:
        area = cv2.contourArea(c)
        print("Area")
        print(area)
        if area > 1000 and area < 1000000:
            print("numero de contronos")
            print(len(contours))

            numero = 0
            for c in contours:
                area = cv2.contourArea(c)
                if area > 1000 and area < 100000000:
                    numero = numero + 1
                    print("El area de la lechuga es: " + str(area))
                    print("El numero de lechugas es: " + str(numero))
