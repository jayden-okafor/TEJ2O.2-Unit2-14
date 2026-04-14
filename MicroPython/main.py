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

# when button "A" is pressed
while True:
    if button_a.was_pressed():
        display.clear()
        loopCounterX = 0
        loopCounterY = 0

        # move the sprite right by 1 each time
        while loopCounterX < 5:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX += 1
            sleep(500)
        loopCounterX -= 1

        # move the sprite down by 1 each time
        while loopCounterY < 5:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY += 1
            sleep(500)
        loopCounterY -= 1

        # move the sprite left by 1 each time
        while loopCounterX >= 0:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX -= 1
            sleep(500)
        loopCounterX += 1

        # move the sprite right by 1 each time
        while loopCounterY >= 0:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY -= 1
            sleep(500)

        # remove sprite and show happy face
        display.clear()
        display.show(Image.HAPPY)

    # when the "B" button is pressed
    if button_b.was_pressed():
        display.clear()
        loopCounterX = 0
        loopCounterY = 0

        # move the sprite down by 1 each time
        while loopCounterY < 5:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY += 1
            sleep(500)
        loopCounterY -= 1

        # move the sprite right by 1 each time
        while loopCounterX < 5:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX += 1
            sleep(500)
        loopCounterX -= 1

        # move the sprite up by 1 each time
        while loopCounterY >= 0:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY -= 1
            sleep(500)
        loopCounterY += 1

        # move the sprite left by 1 each time
        while loopCounterX >= 0:
            display.clear()
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX -= 1
            sleep(500)

        # remove sprite and show happy face
        display.clear()
        display.show(Image.HAPPY)
