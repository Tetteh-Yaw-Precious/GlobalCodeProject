from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
pir = MotionSensor(4)

def PIRDetection():
    if pir.motion_detected:
        GPIO.output(3,GPIO.HIGH)
        print("Motion detected!")
        return 1
    else:
        GPIO.output(3,GPIO.LOW)
        return 0
