# Author: Aditya Manoj Balsane
# Created on: 12/01/2021


import os
import time
import sys



def clickPicture():
    print("-" * 50)
    print("Default path for saving images: /home/pi/Pictures/")
    filename = input("\nEnter a name for saving the image: ")

    load = "Loading Camera Module....\nGathering info from CSI port.... \nDone!"
    

    for char in load:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


    print("\nCamera orientation options:")
    print("1. Original")
    print("2. Vertical Flip")
    print("3. Horizontal Flip")
    print("4. Vertical And Horizontal Flip")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        os.system("raspistill -o /home/pi/Pictures/" + filename + ".jpg")
    elif choice == "2":
        os.system("raspistill -vf -o /home/pi/Pictures/" + filename + ".jpg")
    elif choice == "3":
        os.system("raspistill -hf -o /home/pi/Pictures/" + filename + ".jpg")
    elif choice == "4":
        os.system("raspistill -vf -hf -o /home/pi/Pictures/" + filename + ".jpg")
    else:
        print("Terminated.")
    
 
