from machine import Pin
from time import sleep

led00 = Pin("LED", Pin.OUT)    # onboard LED
#led01 = Pin("GPIO0", Pin.OUT)

led00.off()
#led01.off()
"""
while True:
	led00.on()
	sleep(0.3)
	led00.off()
	sleep(0.3)
"""
