#Robot Car with Camera runs on Raspberry Pi 3 Model B+ and controlled by an Android app.
#Programmed for CITSA UCC Exhibition 2019 by Samuel Bonney & P. K Erbynn
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#setting the physical gpio pins numbers
enA = 11
enB = 12
IN1 = 13 
IN2 = 15 
IN3 = 16 
IN4 = 18 

#setting pins of the motor as output
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

#setting speed of the motor
speedOfMotorA = GPIO.PWM(enA, 255)
speedOfMotorB = GPIO.PWM(enB, 255) 

#selecting percentage of the motor speed to run
speedOfMotorA.start(0) #0 means 0% out of 255 speed is selected
speedOfMotorB.start(0) #0 means 0% out of 255 speed is selected

def backward():   #A Function to move the car backward
        speedOfMotorA.ChangeDutyCycle(25) #25 means 25% out of 255 speed is selected
        speedOfMotorB.ChangeDutyCycle(25) #25 means 25% out of 255 speed is selected
        print("Car moving backward \n")
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
        GPIO.output(IN3, False)
        GPIO.output(IN4, True)             
        GPIO.output(enA, True)   #Enabling car to move
        GPIO.output(enB, True)   #Enabling car to move
  
def forward():   #A Function to move the car foward
    speedOfMotorA.ChangeDutyCycle(25) #25 means 50% out of 255 speed is selected
    speedOfMotorB.ChangeDutyCycle(25) #25 means 50% out of 255 speed is selected
    print("Car moving foward \n")
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)      
    GPIO.output(enA, True)     #Enabling car to move
    GPIO.output(enB, True)    #Enabling car to move

def turnLeft():   #A Function to cause car to turn left
    speedOfMotorA.ChangeDutyCycle(25) #50 means 25% out of 255 speed is selected
    speedOfMotorB.ChangeDutyCycle(25) #50 means 25% out of 255 speed is selected
    print("Car moving Left \n")
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    GPIO.output(enA, True)     #Enabling car to move
    GPIO.output(enB, True)     #Enabling car to move
    sleep(2)   
      
def turnRight():   #A Function to cause car to turn right
    speedOfMotorA.ChangeDutyCycle(25) #25 means 50% out of 255 speed is selected
    speedOfMotorB.ChangeDutyCycle(25) #25 means 50% out of 255 speed is selected
    print("Car moving Right \n")
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    GPIO.output(enA, True)     #Enabling car to move
    GPIO.output(enB, True)     #Enabling car to move
    sleep(2)
   
def stop():   #A Function to stop the car
    print("Car Stopped \n")
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, True)