def on_received_number(receivedNumber):
    radio.send_number(receivedNumber)
    led.set_brightness(255)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.pause(2000)
    basic.clear_screen()
radio.on_received_number(on_received_number)

radio.set_group(1)
radio.set_transmit_power(7)

def on_forever():
    pass
basic.forever(on_forever)
