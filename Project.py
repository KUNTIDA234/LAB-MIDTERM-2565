from tkinter import *
from tkinter import ttk as tk
from tkinter import messagebox

window = Tk()
window.title("Cheaper")
window.geometry('750x600')
#window.iconbitmap('2.ico')
window.configure(bg='#fcdcab')
window.resizable(0,0)

#ราคาหารสินค้า
#ฟังค์ชันในการเช็๋คราคา
def better_Value():
    global result_A_Label,result_B_Label,result_low_price,value_result_A,value_result_B,low_price
    try:
        a = float(Value_text1.get())
        a1 = float(Value_text2.get())
        b = float(Value_text3.get())
        b1 = float(Value_text4.get())
        c = a1/a
        c1 = b1/b
        if (c < c1):
            value_result_A = ("ราคาสินค้า A ราคา {:.3f} บาทต่อหน่วย".format(c))
            value_result_B = ("ราคาสินค้า B ราคา {:.3f} บาทต่อหน่วย".format(c1))
            low_price = ("ราคาสินค้า A ถูกกว่า")
            result_A_Label = Label(font=('Kanit',18),fg='#008000',text=value_result_A,bg='#fcdcab')
            result_A_Label.place(x=200,y=300)
            result_B_Label = Label(font=('Kanit',18),fg='#FF0000',text=value_result_B,bg='#fcdcab')
            result_B_Label.place(x=200,y=350)
            result_low_price = Label(font=('Kanit',18),text=low_price,bg='#fcdcab')
            result_low_price.place(x=270,y=400)
        elif (c1 < c):
            value_result_A = ("ราคาสินค้า A ราคา {:.3f} บาทต่อหน่วย".format(c))
            value_result_B = ("ราคาสินค้า B ราคา {:.3f} บาทต่อหน่วย".format(c1))
            low_price = ("ราคาสินค้า B ถูกกว่า")
            result_A_Label = Label(font=('Kanit',18),fg='#FF0000',text=value_result_A,bg='#fcdcab')
            result_A_Label.place(x=200,y=300)
            result_B_Label = Label(font=('Kanit',18),fg='#008000',text=value_result_B,bg='#fcdcab')
            result_B_Label.place(x=200,y=350)
            result_low_price = Label(font=('Kanit',18),text=low_price,bg='#fcdcab')
            result_low_price.place(x=270,y=400)
        elif (c == c1):
            value_result_A = ("ราคาสินค้า A ราคา {:.3f} บาทต่อหน่วย".format(c))
            value_result_B = ("ราคาสินค้า B ราคา {:.3f} บาทต่อหน่วย".format(c1))
            low_price = ("ราคาสินค้า A และ B เท่ากัน")
            result_A_Label = Label(font=('Kanit',18),text=value_result_A,bg='#fcdcab')
            result_A_Label.place(x=200,y=300)
            result_B_Label = Label(font=('Kanit',18),text=value_result_B,bg='#fcdcab')
            result_B_Label.place(x=200,y=350)
            result_low_price = Label(font=('Kanit',18),text=low_price,bg='#fcdcab')
            result_low_price.place(x=270,y=400)

        btn_submit['state'] = DISABLED
    except:
        messagebox.showwarning('ผิดพลาด','กรุณากรอกตัวเลขเท่านั้น')
        btn_submit['state'] = NORMAL

    return

#ล้างข้อมูล
def btn_clear():
    btn_submit['state'] = NORMAL
    result_A_Label.destroy()
    result_B_Label.destroy()
    result_low_price.destroy()
    Value_text1.delete(0,100)
    Value_text2.delete(0,100)
    Value_text3.delete(0,100)
    Value_text4.delete(0,100)


#บอกข้อความ
Label1 = Label(font=('Kanit',15),text="ขนาดสินค้า A",bg='#fcdcab')
Label1.place(x=50,y=100)
Label2 = Label(font=('Kanit',15),text="หน่วย",bg='#fcdcab')
Label2.place(x=325,y=100)
Label3 = Label(font=('Kanit',15),text="ราคาสินค้า A",bg='#fcdcab')
Label3.place(x=400,y=100)
Label4 = Label(font=('Kanit',15),text="บาท",bg='#fcdcab')
Label4.place(x=680,y=100)
Label5 = Label(font=('Kanit',15),text="ขนาดสินค้า B",bg='#fcdcab')
Label5.place(x=50,y=160)
Label6 = Label(font=('Kanit',15),text="หน่วย",bg='#fcdcab')
Label6.place(x=325,y=160)
Label7 = Label(font=('Kanit',15),text="ราคาสินค้า B",bg='#fcdcab')
Label7.place(x=400,y=160)
Label8 = Label(font=('Kanit',15),text="บาท",bg='#fcdcab')
Label8.place(x=680,y=160)
Label9 = Label(font=('Kanit',20),text="เปรียบเทียบราคาสินค้า",bg='#fcdcab')
Label9.place(x=230,y=25)

#ช่องใส่ข้อความ
Value_text1 = tk.Entry(font=('Kanit'))
Value_text1.place(height=30,width=150,x=170,y=105)
Value_text2 = tk.Entry(font=('Kanit'))
Value_text2.place(height=30,width=150,x=520,y=105)
Value_text3 = tk.Entry(font=('Kanit'))
Value_text3.place(height=30,width=150,x=170,y=165)
Value_text4 = tk.Entry(font=('Kanit'))
Value_text4.place(height=30,width=150,x=520,y=165)

#ปุ่ม
btn_submit = Button(fg='white',font=('Kanit'),anchor=CENTER,text="คำนวณราคา",state=NORMAL,command=better_Value,bg="#4CBB17")
btn_submit.place(height=35,width=150,x=150,y=250)
btn_clear = Button(fg='white',font=('Kanit'),anchor=CENTER,text="ล้างข้อมูล",command=btn_clear,bg="red")
btn_clear.place(height=35,width=150,x=450,y=250)

window.mainloop()
