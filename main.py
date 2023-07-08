#import the GPIO and time package
import RPIO
import time

def a_key_callback(gpio_id, val):
    print("gpio %s: %s" % (gpio_id, val))

# GPIO interrupt callbacks
RPIO.add_interrupt_callback(7, a_key_callback)

while(1):
    time.sleep(2)
