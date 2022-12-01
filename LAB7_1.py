from pyfirmata import Arduino,util
from time import sleep

board = Arduino("COM4")

ledPin = board.get_pin("d:13:o")
ledPin.write(0)

while True:
    ledPin.write(1)
    sleep(0.3)
    ledPin.write(0)
    sleep(0.2)

board.exit()
