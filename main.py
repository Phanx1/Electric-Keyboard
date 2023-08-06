#import the GPIO and time package
import RPIO
import time
import playsound

def a_key_callback(gpio_id, val):
    print("gpio: ", gpio_id, "value: ", val)
    playsound.playsound('prep_pianoC4.wav')

# GPIO interrupt callbacks
RPIO.add_interrupt_callback(7, a_key_callback)

while(1):
    time.sleep(2)
