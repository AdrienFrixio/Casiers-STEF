from machine import Pin
import time

buzzer = Pin(33, Pin.OUT)

def buzz(timing):
    buzzer.value(1)
    time.sleep(timing)
    buzzer.value(0)
    time.sleep(timing)