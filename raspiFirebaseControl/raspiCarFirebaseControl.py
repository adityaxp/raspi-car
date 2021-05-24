# Author: Aditya Manoj Balsane
# Created on: 23/05/2021

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import RPi.GPIO as GPIO
import time


cred = credentials.Certificate("/home/pi/raspi-car/raspiFirebaseControl/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL" : "https://raspi-car-internet-control-default-rtdb.asia-southeast1.firebasedatabase.app/"
})





def firebaseControl():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        while True:
            time.sleep(1)
            ref = db.reference('raspi-car/carState')
            if ref.get() == "W":
                print("Current State: Moving Forward")
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, True)
                GPIO.output(15, False)
            elif ref.get() == "A":
                print("Current State: Moving Right")
                GPIO.output(7, False)
                GPIO.output(11, True)
                GPIO.output(13, True)
                GPIO.output(15, False)
            elif ref.get() == "D":
                print("Current State: Moving Left")
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, True)
            elif ref.get() == "S":
                print("Current State: Moving Backward")
                GPIO.output(7, False)
                GPIO.output(11, True)
                GPIO.output(13, False)
                GPIO.output(15, True)
            elif ref.get() == "Stationary":
                print("Current State: " + ref.get())
                GPIO.output(7, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)

    except KeyboardInterrupt:
        print("No errors just a dumb and inefficient way to break the loop because I'm lazy :)")

            
    finally:
        GPIO.cleanup()
        print("GPIO CLEARED")

        



    




    





