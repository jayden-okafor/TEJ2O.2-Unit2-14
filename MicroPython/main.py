# Copyright (c) 2026 MTHS All rights reserved
#
# Created by: Jayden Okafor
# Created on: Apr 2026
# This program sets a countdown using the microbit, and turns on that many neopixels

from microbit import *

# variables
loopCounterX = 0
loopCounterY = 0

# show happy face
display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.was_pressed():
        display.clear()
        loopCounterX = 0
        loopCounterY = 0

        while loopCounterX < 5:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX += 1
            sleep(500)

        loopCounterX -= 1  # fix position

        while loopCounterY < 5:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY += 1
            sleep(500)

        loopCounterY -= 1  # fix position

        while loopCounterX >= 0:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX -= 1
            sleep(500)

        loopCounterX += 1  # fix position

        while loopCounterY >= 0:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY -= 1
            sleep(500)

        display.clear()
        display.show(Image.HAPPY)

    if button_b.was_pressed():
        display.clear()
        loopCounterX = 0
        loopCounterY = 0

        while loopCounterY < 5:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY += 1
            sleep(500)

        loopCounterY -= 1

        while loopCounterX < 5:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX += 1
            sleep(500)

        loopCounterX -= 1

        while loopCounterY >= 0:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY -= 1
            sleep(500)

        loopCounterY += 1

        while loopCounterX >= 0:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX -= 1
            sleep(500)

        display.clear()
        display.show(Image.HAPPY)

