from tkinter import *
window = Tk()
window.title("โปรแกรมหาพื้นที่")
window.resizable(0,0)
window.geometry("300x350")
var = IntVar()
def sum():
    ck = var.get()
    if  ck == 1:
        a = float(Value1.get())
        b = float(Value2.get())
        s = 0.5*a*b
        result = Label(window,text=s,font=("TH SarabunPSK",16))
        result.grid(column=3,row=20)
    if  ck == 2:
        a = int(Value1.get())
        b = int(Value2.get())
        s = a*b
        result = Label(window,text=s,font=("TH SarabunPSK",16))
        result.grid(column=3,row=20)
    return

v1 = Radiobutton(window,text = "หาพื้นที่สามหลี่ยม",font=("TH SarabunPSK",16),variable=var,value=1)
v1.grid(column=0,row=1)
v2 = Radiobutton(window,text = "หาพื้นที่สี่เหลี่ยม",font=("TH SarabunPSK",16),variable=var,value=2)
v2.grid(column=0,row=2)
Label1 = Label(window,text="ความสูง/ยาว",font=("TH SarabunPSK",16))
Label1.grid(column=0,row=3)
Value1 = Entry(window,width=24)
Value1.grid(column=3,row=3)
Label2 = Label(window,text="ฐาน/กว้าง",font=("TH SarabunPSK",16))
Label2.grid(column=0,row=8)
Value2 = Entry(window,width=24)
Value2.grid(column=3,row=8)
Label3 = Label(window,text="ผลลัพธ์",font=("TH SarabunPSK",16))
Label3.grid(column=0,row=20)
btn_sum = Button(window,text="หาพื้นที่",font=("TH SarabunPSK",15),command=sum)
btn_sum.grid(column=3,row=10)

window.mainloop()