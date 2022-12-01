from tkinter import *
from tkinter import messagebox
from os import *
window = Tk()
window.geometry('200x100')
window.title("Welcome")
lbl = Label(window, text = "Password : ")
lbl.grid(column=0,row=0)
# ประกาศใช้ Textbox จากคลาส Entry
txt = Entry(window,width=10)
txt.grid(column=1,row=0)

def btn_clicked():
    # แสดงค่าบน label
    lbl.configure(text="Button was clicked !!")
    # แสดงค่าบน messagebox
    messagebox.showinfo("Display","Clicked!!!")
    
btn = Button(window,text="Click",command=btn_clicked)

btn.grid(column=1,row=1)
window.mainloop()
