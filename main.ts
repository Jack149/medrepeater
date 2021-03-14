radio.onReceivedNumber(function (receivedNumber) {
    basic.pause(200)
    radio.sendNumber(receivedNumber)
    led.setBrightness(255)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.pause(2000)
    basic.clearScreen()
})
radio.setGroup(1)
radio.setTransmitPower(7)
basic.forever(function () {
	
})
