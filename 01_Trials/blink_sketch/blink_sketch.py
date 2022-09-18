import pyfirmata
import time
import serial

board = pyfirmata.Arduino('/dev/tty.usbserial-1420')
data = input("blink? ")

if data == "true":
    while True:
        board.digital[13].write(1)
        time.sleep(0.1)
        board.digital[13].write(0)
        time.sleep(0.1)