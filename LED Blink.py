import machine
import time

#Configure LED pin as OUTPUT pin
led = machine.Pin("LED",machine.Pin.OUT);
while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)