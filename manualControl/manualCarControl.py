import curses
import RPi.GPIO as GPIO
import time

    
def manualControl():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    screen = curses.initscr()
    curses.noecho() 
    curses.cbreak()
    screen.keypad(True)
    try:
        while True:
            
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                print("Accelerate")
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, True)
                GPIO.output(15, False)
                time.sleep(1)
            elif char == curses.KEY_UP:
                print("Accelerate")
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, True)
                GPIO.output(15, False)
                time.sleep(1)
            elif char == curses.KEY_RIGHT:
                print("Right Turn")
                GPIO.output(7, False)
                GPIO.output(11, True)
                GPIO.output(13, True)
                GPIO.output(15, False)
                time.sleep(1)
            elif char == curses.KEY_LEFT:
                print("Left Turn")
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, True)
                time.sleep(1)
            elif char == curses.KEY_DOWN:
                print("Reverse")
                GPIO.output(7, False)
                GPIO.output(11, True)
                GPIO.output(13, False)
                GPIO.output(15, True)
                time.sleep(1)
            elif char == 10:
                GPIO.output(7, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)    
        
    finally:
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        GPIO.cleanup()
        print("GPIO CLEARED")
    

        
            
        
