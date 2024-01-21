#!/usr/bin/env python3
#import the GPIO and time package

#using red button
import RPi.GPIO as GPIO
import time
import playsound
from threading import Thread, Lock

second_from_bottom_inside = 2
class piano_key():
    def __init__(self, gpio_number):
        print("start init")
        self.lockc4 = Lock()
        self.x = Thread(target=self.play_note)
        self.x.start()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_number, GPIO.IN)
        GPIO.add_event_detect(gpio_number, GPIO.BOTH, callback=self.a_key_callback, bouncetime=5)
        print("done init")
        
    def a_key_callback(self, channel):
        if GPIO.input(second_from_bottom_inside):
            print("GPIO released")
            if self.lockc4.locked():
                self.lockc4.release()
            
        else:
            print("gpio pressed")
            self.lockc4.acquire(False)

    def play_note(self):
        while (1):
            if self.lockc4.locked():
                playsound.playsound('prep_pianoC4.wav')
        
def main():
    # GPIO interrupt callbacks
    first_key = piano_key(second_from_bottom_inside)
    
    while(1):
        time.sleep(2)

if __name__ == '__main__':
    main()
