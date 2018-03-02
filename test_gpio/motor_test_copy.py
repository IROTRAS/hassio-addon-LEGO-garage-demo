#!/usr/bin/python

# Declare Imports
import os
#import time
#import threading
import RPi.GPIO as GPIO
#import random

print("Starting the script........")

# ingore any warnings
GPIO.setwarnings(False)

# Declare variables
GPIO.setmode(GPIO.BCM)

# motor inputs
GPIO_STBY = 12
GPIO_PWMA = 13
GPIO_AIN2 = 5
GPIO_AIN1 = 6 
GPIO_PWMB = 19
GPIO_BIN2 = 16
GPIO_BIN2 = 20

motor_time = 1
# proportion for which the Motor is ON over the total time
dutycycle = .2

# This Function drives Motor A for period of time

# setup GPIO pins
GPIO.setup(GPIO_PWMA,GPIO.OUT)
GPIO.setup(GPIO_AIN2,GPIO.OUT)
GPIO.setup(GPIO_AIN1,GPIO.OUT)
GPIO.setup(GPIO_STBY,GPIO.OUT)
# Set the PWM for pins
pwmA = GPIO.PWM(GPIO_PWMA, 25000)



#Drive the Motors direction
GPIO.output(GPIO_AIN2,False)
GPIO.output(GPIO_AIN1,True)
#set standby pin
GPIO.output(GPIO_STBY,True)
#Set the motor speed
GPIO.output(GPIO_PWMA, True)
pwmA.start(dutycycle)

# on for motor time
time.sleep(motor_time)
# Reset all motors to shut off
GPIO.output(GPIO_PWMA,False)
GPIO.output(GPIO_AIN2,False)
GPIO.output(GPIO_AIN1,False)
GPIO.output(GPIO_STBY,False)
time.sleep(motor_time)

pwmA.stop()
GPIO.cleanup()

# -----------------------
# Main Program
# -----------------------
