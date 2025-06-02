import time 
from machine import Pin
from myneopixel import Neopixel

pixels = Neopixel(15, 0, 17)
pixels.brightness(255)
pixels.fill((255, 0, 0))
pixels.show()
time.sleep(2)