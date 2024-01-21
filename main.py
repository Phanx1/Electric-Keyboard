#!/usr/bin/env python3
#import the GPIO and time package

#using red button
import RPi.GPIO as GPIO
import time
import simpleaudio as sa
from threading import Thread, Lock

second_from_bottom_inside = 2
GPIO_3 = 3
class piano_key():
    def __init__(self, gpio_number, direction):
        print("start init")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_number, GPIO.IN)
        GPIO.add_event_detect(gpio_number, GPIO.BOTH, callback=self.a_key_callback, bouncetime=5)
        self.wave_obj = sa.WaveObject.from_wave_file("prep_pianoC4.wav")
        self.play_obj = 0
        self.direction = direction
        self.gpio = gpio_number
        print("done init")
        
    def a_key_callback(self, channel):
        if self.direction:
            if GPIO.input(self.gpio):
                print("GPIO released")
                if self.play_obj.is_playing():
                    self.play_obj.stop()
            else:
                print("gpio pressed")
                self.play_obj = self.wave_obj.play()
        else:
            if GPIO.input(self.gpio):
                print("gpio pressed")
                self.play_obj = self.wave_obj.play()  
            else:
                print("GPIO released")
                if self.play_obj.is_playing():
                    self.play_obj.stop()
        
def main():
    # GPIO interrupt callbacks
    first_key = piano_key(second_from_bottom_inside, True)
    second_key = piano_key(GPIO_3, False)
    
    while(1):
        time.sleep(2)

if __name__ == '__main__':
    main()
