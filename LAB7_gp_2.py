from distutils.command.config import config
from tkinter import *
import pyfirmata
import time
import random

window = Tk()
window.geometry("300x300")
window.resizable(0,0)
window.title("VR LED")

board = pyfirmata.Arduino('COM5')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

def Ledbutton():
    ledPin1 = board.get_pin("d:13:o")
    ledPin1.write(0)
    ledPin2 = board.get_pin("d:12:o")
    ledPin2.write(0)
    ledPin3 = board.get_pin("d:11:o")
    ledPin3.write(0)
    ledPin4 = board.get_pin("d:10:o")
    ledPin4.write(0)
    ledPin5 = board.get_pin("d:9:o")
    ledPin5.write(0)
    ledPin6 = board.get_pin("d:8:o")
    ledPin6.write(0)
    ledPin7 = board.get_pin("d:7:o")
    ledPin7.write(0)
    ledPin8 = board.get_pin("d:6:o")
    ledPin8.write(0)

    while True:
        Button_LED['state'] = DISABLED
        ledPin1.write(1)
        time.sleep(0.3)
        ledPin1.write(0)
        time.sleep(0.2)
        ledPin2.write(1)
        time.sleep(0.3)
        ledPin2.write(0)
        time.sleep(0.2)
        ledPin3.write(1)
        time.sleep(0.3)
        ledPin3.write(0)
        time.sleep(0.2)
        ledPin4.write(1)
        time.sleep(0.3)
        ledPin4.write(0)
        time.sleep(0.2)
        ledPin5.write(1)
        time.sleep(0.3)
        ledPin5.write(0)
        time.sleep(0.2)
        ledPin6.write(1)
        time.sleep(0.3)
        ledPin6.write(0)
        time.sleep(0.2)
        ledPin7.write(1)
        time.sleep(0.3)
        ledPin7.write(0)
        time.sleep(0.2)
        ledPin8.write(1)
        time.sleep(0.3)
        ledPin8.write(0)
        time.sleep(0.2)
        Button_LED['state'] = NORMAL
        board.exit()

def vr_color():
        analog_value = analog_input.read()
        if analog_value == 1.0:
            Button_vr.configure(bg='red')
        elif analog_value == 0:
            Button_vr.configure(bg='green')

Button_LED = Button(window,text="LED",font=14,bg="red",command=Ledbutton)
Button_LED.place(x=125,y=50)

Button_vr = Button(window,text="VR CHECK",font=20,command=vr_color)
Button_vr.place(x=90,y=150)

window.mainloop()

