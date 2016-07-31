#!/usr/bin/env python
import webiopi
import RPi.GPIO as io


io.setwarnings(False)
io.setmode(io.BCM)

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








pins = (m1a,m1b,m2a,m2b,luces)
for i in pins:
   io.setup(i,io.OUT)


@webiopi.macro
def Forward():
   io.output(m1b,False)
   #io.output(m2b,False)
   io.output(m1a,True)
   #io.output(m2a,True)

@webiopi.macro
def Retroceder():
   io.output(m1b,True)
   #io.output(m2b,True)
   io.output(m1a,False)
   #io.output(m2a,False)

@webiopi.macro
def Derecha():
   io.output(m2a,True)
   io.output(m2b,False)

@webiopi.macro
def Izquierda():
   io.output(m2a,False)
   io.output(m2b,True)

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
