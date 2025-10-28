import machine
import time

#Configure LED pin as OUTPUT pin
led = machine.Pin(15,machine.Pin.OUT);
while True:
    led.toggle()
    time.sleep(0.1)

