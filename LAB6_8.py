import imp
from tkinter import * 
window = Tk()
btnRed = Button(window,text="Red",fg="red")
btnRed.pack(side=LEFT)
btnGreen = Button(window,text="Green",fg="green")
btnGreen.pack(side=RIGHT)
btnBlue = Button(window,text="Blue",fg="blue")
btnBlue.pack(side=TOP)
btnBlack = Button(window,text="Black",fg="black")
btnBlack.pack(side=BOTTOM)
window.mainloop()