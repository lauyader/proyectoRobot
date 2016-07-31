#!/usr/bin/env python
import webiopi
import RPi.GPIO as io      # Importamos la conexion con GPIO Raspberry
import time                #Importamos time (time.sleep)
import pygame               # Importamos las aplicaciones pygame, activar el audio

io.setwarnings(False)
io.setmode(io.BCM)
################################
# Incio de la libreria de audio
################################
pygame.mixer.init()

################################
# Declaracion del gpio 15 para el audio
################################
GPIO_luz = 15
GPIO.setup(GPIO_luz, GPIO.OUT)
GPIO.output(GPIO_luz,False)


#############################################
#Declaracion de la variables de  los leds-PIN-GPIO
############################################

luces =15
m1a = 18
m1b = 17
m2a = 6
m2b = 13

    #assume motor1 forward  is  m1a=True  m1b=False
    #assume motor1 backward is  m1a=False m1b=True
    #assume motor2 forward  is  m2a=True  m2b=False
    #assume motor2 backward is  m2a=False m2b=True

################################
# Declaracion del sensor ultrasonido
################################

GPIO_TRIGGER = 9          #Usamos el pin GPIO 25 como TRIGGER
GPIO_ECHO    = 10           #Usamos el pin GPIO 7 como ECHO
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  #Configuramos Trigger como salida
GPIO.setup(GPIO_ECHO,GPIO.IN)      #Configuramos Echo como entrada
GPIO.output(GPIO_TRIGGER,False)    #Ponemos el pin 25 como LOW







pins = (m1a,m1b,m2a,m2b,luces)
for i in pins:
   io.setup(i,io.OUT)
################################
# Sensor de ultrasonidos
################################
@webiopi.macro
def Ultrasonido_Inicio():

        while True:     #Iniciamos un loop infinito
                GPIO.output(GPIO_TRIGGER,True)   #Enviamos un pulso de ultrasonidos
                time.sleep(0.00001)              #Una pequeñña pausa
                GPIO.output(GPIO_TRIGGER,False)  #Apagamos el pulso
                start = time.time()              #Guarda el tiempo actual mediante time.time()
                while GPIO.input(GPIO_ECHO)==0:  #Mientras el sensor no reciba señal...
                    start = time.time()          #Mantenemos el tiempo actual mediante time.time()
                while GPIO.input(GPIO_ECHO)==1:  #Si el sensor recibe señal...
                    stop = time.time()           #Guarda el tiempo actual mediante time.time() en otra variable
                elapsed = stop-start             #Obtenemos el tiempo transcurrido entre envío y recepción
                distance = (elapsed * 34300)/2   #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
        #        print round(distance,2)                   #Devolvemos la distancia (en centímetros) por pantalla
        #        with open('data.csv', 'w') as csvfile:
        #            spamwriter = csv.writer(csvfile, delimiter=' ',
        #                                     quoting=csv.QUOTE_MINIMAL)
                    #spamwriter.writerow(['Spam'] * 4 + ['Baked Beans'])
                    #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        #            spamwriter.writerow([lista] )
        #            lista.append(distance)
        #            print lista


        # Se le incorpora AUDIO


        if distance<40:
            GPIO.output(GPIO_luz,True)
            pygame.mixer.music.load("cuidado.wav")
        	pygame.mixer.music.play()
            print "Obstaculo en en la vía"
        else:
        	GPIO.output(GPIO_luz,False)
        	pygame.mixer.music.load("continuar.wav")
            pygame.mixer.music.play()

        if distance>42:
        	pygame.mixer.music.stop()

        time.sleep(1)

@webiopi.macro
def Ultrasonido_Parar():
    GPIO.cleanup()


################################
# Control de Avance
################################

@webiopi.macro
def Forward():
   io.output(m1b,False)
   #io.output(m2b,False)
   io.output(m1a,True)
   #io.output(m2a,True)

################################
# Control de Retroceso
################################
@webiopi.macro
def Retroceder():
   io.output(m1b,True)
   #io.output(m2b,True)
   io.output(m1a,False)
   #io.output(m2a,False)

################################
# Cruzar a la Derecha e Izquierda
################################
@webiopi.macro
def Derecha():
   io.output(m2a,True)
   io.output(m2b,False)

@webiopi.macro
def Izquierda():
   io.output(m2a,False)
   io.output(m2b,True)

################################
# Parar el vehículo
################################
@webiopi.macro
def Stop():
   io.output(m1b,False)
   io.output(m2b,False)
   io.output(m1a,False)
   io.output(m2a,False)


#########################################
# Operacion con las luces
##########################################
@webiopi.macro
def Luces():
   io.output(luces,True)
@webiopi.macro
def ApagarLuces():
   io.output(luces,False)


Stop()
