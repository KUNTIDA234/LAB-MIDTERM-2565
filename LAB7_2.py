import pyfirmata
from time import sleep

board = pyfirmata.Arduino('COM4')

led = board.get_pin('d:11:p')

value = 0.0
while True:
    value += 0.01
    if value >= 1.0: value = 0.0
    led.write(value)
    sleep(0.05)

board.exit()