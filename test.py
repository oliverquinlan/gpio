from gpiozero import PiLiter
from signal import pause

lite = PiLiter()

lite.blink()

pause()
