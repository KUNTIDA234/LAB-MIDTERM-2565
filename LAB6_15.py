import tkinter as tk

window = tk.Tk()
window.geometry('160x100')
window.title("Calculator")
lbl1 = tk.Label(window,text="value A : ")
lbl1.grid(column=0,row=0)
lbl2 = tk.Label(window,text="value B : ")
lbl2.grid(column=0,row=1)
txt1 = tk.Entry(window,width=15)
txt1.grid(column=1,row=0)
txt2 = tk.Entry(window,width=15)
txt2.grid(column=1,row=1)
lblResult = tk.Label(window)
lblResult.grid(column=1,row=3)

def btn_clicked():
    n1 = int(txt1.get())
    n2 = int(txt2.get())
    result = n1 + n2
    lblResult.configure(text=str(result))
    # หรือ อาจใช้ lblResult.config(text=str(result))
    print(result)

btn = tk.Button(window,text="Add",width=12,command=btn_clicked)
btn.grid(column=1,row=2)
window.mainloop()
