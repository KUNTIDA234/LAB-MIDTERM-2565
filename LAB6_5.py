from tkinter import * 
window = Tk()
window.title("My Title")
window.geometry("640x480")
lbl = Label(window, text="Label",font=("Arial Bold",30))
lbl.grid(column=0,row=0)
btn = Button(window, text ="Click Me",font=("Arial",40))
btn.grid(column=0,row=1)
window.mainloop()
