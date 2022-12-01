from tkinter import *
from tkinter import messagebox
from os import *
window = Tk()
window.geometry('200x100')
window.title("Welcome")
lbl = Label(window, text = "Password : ")
lbl.grid(column=0,row=0)

def btn_clicked():
    messagebox.showinfo("Display","you type " + txt.get())

btn = Button(window,text="Click",command=btn_clicked)
btn.grid(column=1,row=1)
txt = Entry(window,width=10)
txt.grid(column=1,row=0)
window.mainloop()
