# Author: Aditya Manoj Balsane
# Created on: 19/05/2021


import RPi.GPIO as GPIO
import time

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)

def forward(tf):
	print("forward")
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(tf)

def rightTurn(tf):
	print("Right Turn")
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(tf)
        
def leftTurn(tf):
	print("Left Turn")
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(13, False)
	GPIO.output(15, True)
	time.sleep(tf)

def backward(tf):
	print("Backward")
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, False)
	GPIO.output(15, True)
	time.sleep(tf)

def gpioCleanUP():
        GPIO.cleanup()
        print("GPIO CLEARED")



