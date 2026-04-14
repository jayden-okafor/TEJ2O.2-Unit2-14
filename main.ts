/* Copyright (c) 2026 MTHS All rights reserved
 *
 * Created by: Jayden Okafor
 * Created on: Apr 2026
 * This program sets a countdown using the microbit, and turns on that many neopixels
*/

// variables
let sprite: game.LedSprite = null
let loopCounterX: number = 0
let loopCounterY: number = 0

// show happy face
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// when button "A" is pressed
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    sprite = game.createSprite(0, 0)
    loopCounterX = 0
    loopCounterY = 0

    // move the sprite right by 1 each time
    while (loopCounterX < 5) {
        sprite.set(LedSpriteProperty.X, loopCounterX)
        loopCounterX++
        basic.pause(500)
    }

    // move the sprite down by 1 each time
    while (loopCounterY < 5) {
        sprite.set(LedSpriteProperty.Y, loopCounterY)
        loopCounterY++
        basic.pause(500)
    }

    // move the sprite left by 1 each time
        while (loopCounterX >= 0) {
            sprite.set(LedSpriteProperty.X, loopCounterX)
            loopCounterX--
            basic.pause(500)
        }

    // move the sprite right by 1 each time
        while (loopCounterY >= 0) {
            sprite.set(LedSpriteProperty.Y, loopCounterY)
            loopCounterY--
            basic.pause(500)
        }

    // remove sprite and show happy face
    sprite.delete()
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
})

// when the "B" button is pressed
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    sprite = game.createSprite(0, 0)
    loopCounterX = 0
    loopCounterY = 0

    // move the sprite down by 1 each time
    while (loopCounterY < 5) {
        sprite.set(LedSpriteProperty.Y, loopCounterY)
        loopCounterY++
        basic.pause(500)
    }

    // move the sprite right by 1 each time
    while (loopCounterX < 5) {
        sprite.set(LedSpriteProperty.X, loopCounterX)
        loopCounterX++
        basic.pause(500)
    }

    // move the sprite up by 1 each time
        while (loopCounterY >= 0) {
            sprite.set(LedSpriteProperty.Y, loopCounterY)
            loopCounterY--
            basic.pause(500)
        }

    // move the sprite left by 1 each time
        while (loopCounterX >= 0) {
            sprite.set(LedSpriteProperty.X, loopCounterX)
            loopCounterX--
            basic.pause(500)
        }

    // remove sprite and show happy face
    sprite.delete()
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
})
