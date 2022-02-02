# Author: Aditya Manoj Balsane
# Created on: 22/05/2021

from raspiCamera import camera
from raspiTest import test
from manualControl import manualCarControl
from raspiFirebaseControl import raspiCarFirebaseControl
import os 

print("-" * 50)
print("Rasberry-Pi Car Control Terminal - By Aditya Balsane")
print("-" * 50)

print("Please choose an operation to continue")
print("1. Click a picture")
print("2. Test car motors")
print("3. Control car offline")
print("4. Control car over internet (Needs Android app to communicate with raspi)")
print("5. Object Detection using openCV and TensorFlow Lite")
print("6. Exit")

choice = input("\n Enter your choice: ")

if choice == "1":
    camera.clickPicture()
elif choice == "2":
    print("-" * 50)
    print("Testing...\nRotating motors in all directions for 5 sec...")
    test.init()
    test.forward(5)
    test.rightTurn(5)
    test.leftTurn(5)
    test.backward(5)
    test.gpioCleanUP()
elif choice == "3":
    print("-" * 50)
    print("Controls: \n/|\ : Move Forward \n<- : Turn Right \n-> : Turn Left \n\|/ : Move Backward \nq: To Exit \nPress ENTER key to start")
    start = input()
    manualCarControl.manualControl()
elif choice == "4":
    print("-" * 50)
    print("Open RaspiCarControl mobile application to control the car and press ENTER to get live car state")
    start = input()
    raspiCarFirebaseControl.firebaseControl()
elif choice == "5":
    print("-" * 50)
    
    os.system("source /home/pi/raspi-car/tflite/tflite-env/bin/activate")
    os.system("python3 /home/pi/raspi-car/tflite/TFLite_detection_webcam.py --modeldir=Sample_TFLite_model")
elif choice == "6":
    print("-" * 50)
    print("Terminated..")
    print("-" * 50)
else:
    print("-" * 50)
    print("Invalid choice...\nPlease try again...")
    print("-" * 50)



    
    
    

    
