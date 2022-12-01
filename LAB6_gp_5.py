from tkinter import *


window = Tk()
window.title("โปรแกรมตัดเกรด")
window.resizable(0,0)
window.geometry("425x500")

def score():
    score = int(value_score.get())
    if (score >= 80):
        r = ("เกรด A")
    elif (score >= 70):
        r = ("เกรด B")
    elif (score >= 60):
        r = ("เกรด C")
    elif (score >= 50):
        r =("เกรด D")
    else:
        r =("เกรด F")
    grade_Label = Label(window,text=r,font=("TH SarabunPSK",25))
    grade_Label.place(x=250,y=220)
    return

Label1 = Label(window,text="ป้อนคะแนน",font=("TH SarabunPSK",30))
Label1.place(x=25,y=100)
value_score = Entry(window,width=20,font=("TH SarabunPSK",18))
value_score.place(x=200,y=105)
btn_score = Button(window,text="ตัดเกรด",font=("TH SarabunPSK",18),width=10,height=1,bg="red",fg="white",command=score)
btn_score.place(x=240,y=150)

window.mainloop()