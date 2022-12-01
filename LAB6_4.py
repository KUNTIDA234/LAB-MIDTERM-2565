from tkinter import * 
window = Tk()
window.title("My Title")
window.geometry("640x480")
lbl = Label(window, text="Hello",font=("Arial Bold",30))
lbl.grid(column=0,row=0)
window.mainloop()
