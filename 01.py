import time
from machine import Pin

led = Pin (1, Pin.OUT)
for i in range(10):
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)
    led.value(0)