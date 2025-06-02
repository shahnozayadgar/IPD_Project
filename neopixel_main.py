# import time 
# from myneopixel import Neopixel

# numpix = 15
# pixels = Neopixel(numpix, 0, 0, "GRB")

# yellow = (255, 100, 0)
# orange = (255, 50, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# red = (255, 0, 0)
# color0 = red

# pixels.brightness(50)
# pixels.fill(orange)
# pixels.set_pixel_line_gradient(3, 13, green, blue)
# # Removed pixels.set_pixel(20, (255, 255, 255)) since you only have 15 LEDs (0-14)
# pixels.show()

# for i in range(5):  # Run only 5 times
#     if color0 == red:
#         color0 = yellow
#         color1 = red
#     else:
#         color0 = red
#         color1 = yellow
#     pixels.set_pixel(0, color0)
#     pixels.set_pixel(1, color1)
#     pixels.show()
#     time.sleep(1)

# print("Animation complete!")

import time 
from myneopixel import Neopixel

# Simple test - just light up first LED red
numpix = 1
pixels = Neopixel(numpix, 0, 2, "BRG")

print("Testing LED...")

# Set first LED to bright red
pixels.set_pixel(0, (255, 0, 0))
pixels.show()

print("LED 0 should be red now")
time.sleep(2)

# Turn off
pixels.set_pixel(0, (0, 0, 0))
pixels.show()

print("LED should be off now")