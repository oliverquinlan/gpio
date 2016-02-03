from gpiozero import PiLiter
from time import sleep

lite = PiLiter()

while True:
    lite.on()
    sleep(1)
    lite.off()
    sleep(1)