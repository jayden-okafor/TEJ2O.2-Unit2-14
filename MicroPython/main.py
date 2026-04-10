# Copyright (c) 2026 MTHS All rights reserved
#
# Created by: Jayden Okafor
# Created on: Apr 2026
# This program sets a countdown using the microbit, and turns on that many neopixels

from microbit import *

# variables
sprite_x = 0
sprite_y = 0
loopCounterX = 0
loopCounterY = 0

# show happy face
display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.was_pressed():
        display.clear()
        sprite_x = 0
        sprite_y = 0
        loopCounterX = 0
        loopCounterY = 0

        while loopCounterX < 5:
            sprite_x = loopCounterX
            display.set_pixel(sprite_x, sprite_y, 9)
            loopCounterX += 1
            sleep(500)

        while loopCounterY < 5:
            sprite_y = loopCounterY
            display.set_pixel(sprite_x, sprite_y, 9)
            loopCounterY += 1
            sleep(500)

        if loopCounterX == 5:
            while loopCounterX >= 0:
                sprite_x = loopCounterX
                display.set_pixel(sprite_x, sprite_y, 9)
                loopCounterX -= 1
                sleep(500)

        if loopCounterY == 5:
            while loopCounterY >= 0:
                sprite_y = loopCounterY
                display.set_pixel(sprite_x, sprite_y, 9)
                loopCounterY -= 1
                sleep(500)

        display.clear()
        display.show(Image.HAPPY)

    if button_b.was_pressed():
        display.clear()
        sprite_x = 0
        sprite_y = 0
        loopCounterX = 0
        loopCounterY = 0

        while loopCounterY < 5:
            sprite_y = loopCounterY
            display.set_pixel(sprite_x, sprite_y, 9)
            loopCounterY += 1
            sleep(500)

        while loopCounterX < 5:
            sprite_x = loopCounterX
            display.set_pixel(sprite_x, sprite_y, 9)
            loopCounterX += 1
            sleep(500)

        if loopCounterY == 5:
            while loopCounterY >= 0:
                sprite_y = loopCounterY
                display.set_pixel(sprite_x, sprite_y, 9)
                loopCounterY -= 1
                sleep(500)

        if loopCounterX == 5:
            while loopCounterX >= 0:
                sprite_x = loopCounterX
                display.set_pixel(sprite_x, sprite_y, 9)
                loopCounterX -= 1
                sleep(500)

        display.clear()
        display.show(Image.HAPPY)
