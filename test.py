from gpiozero import PiLiter
from time import sleep

lite = PiLiter()
lite.off()

while True:
    for led in lite.leds:
        led.on()
        sleep(0.1)
        led.off()
