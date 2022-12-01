from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("My first GUI App")
window.geometry("640x480")
lbl = Label(window, text="Hello")
lbl.grid(column=0,row=0)

def clicked():
    messagebox.showinfo("Message title","Button is clicked")

btn = Button(window,text="Click Me", command=clicked)
btn.grid(column=1,row=0)
window.mainloop()
