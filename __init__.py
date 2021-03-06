from mycroft import MycroftSkill, intent_file_handler
import RPi.GPIO as GPIO
import time 
from time import sleep

in1 = 17 # R Motor GPIO address
#GPIO 17 = wPi , BCM 8, phys addr = 18
in2 = 27 # R Motor GPIO address
#GPIO 27 = wPi 14, BCM 11, phys addr = 16
in3 = 23 # L Motor GPIO address
#GPIO 17 = wPi 0, BCM 17, phys addr = 11
in4 = 24 # L Motor GPIO address
#GPIO 27 = wPi 2, BCM 27, phys addr = 13
en = 25 #L motor gpio
#GPIO 8 = wPi  , BCM 
en2 = 22 #R MOTOR GPIO
#GPIO 22 = wPi 3, BCM 22, phys addr = 15
temp1=1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)


class Tankstop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tankstop.intent')
    def handle_tankstop(self, message):
        self.speak_dialog('tankstop')

        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
             
def create_skill():
    return Tankstop()

