import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

servoPIN = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # Physical pin 3 for PWM with 50Hz
p.start(0) # Initialization

def moveServoLeft():
    print('Servo Moves Left')
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    print('Servo moves left')
    p.ChangeDutyCycle(12.5)
    time.sleep(3)
    print('Servo moves 6')
    p.ChangeDutyCycle(0)
    time.sleep(2)
    p.start(0)
    
def moveServoRight():
    print('Servo Moves Right')
    print('Servo moves 8')
    p.ChangeDutyCycle(2.5)
    time.sleep(3)
    print('Servo moves 2')
    p.ChangeDutyCycle(7.5)
    time.sleep(2)
    p.start(0)
    
def moveServoLeftToRight():
    moveServoLeft()
    moveServoRight()