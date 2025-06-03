from machine import Pin
import utime

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("Button pressed!")
        utime.sleep(1)