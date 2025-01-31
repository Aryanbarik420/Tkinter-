from tkinter import *
 

win=Tk()



data=""

def get_data(value):
    global data
    data=data+str(value)
    var.set(data)

def equal_data():
    global data

    total=str(eval(data))
    var.set(total)

def clear():
    global data

    data=""
    var.set(data)

win.title("Calculator")
win.config(bg="cyan")


win.geometry("500x570")
win.resizable(False,False)


label_title=Label(win,text="Calculator",font=("Times New Roman",20,"bold"))
label_title.place(x=90,y=20,height=70,width=320)

var=StringVar()
entry=Entry(win,relief="sunken",font=("Times New Roman",20,"bold"),bd=5,textvariable=var)
entry.place(x=20,y=110,height=60,width=460)



but_1=Button(win,text="1",font=("Times New Roman",20,"bold"),command=lambda:get_data(1))
but_1.place(x=20,y=190,height=70,width=115)

but_2=Button(win,text="2",font=("Times New Roman",20,"bold"),command=lambda:get_data(2))
but_2.place(x=135,y=190,height=70,width=115)

but_3=Button(win,text="3",font=("Times New Roman",20,"bold"),command=lambda:get_data(3))
but_3.place(x=250,y=190,height=70,width=115)

but_add=Button(win,text="+",font=("Times New Roman",20,"bold"),command=lambda:get_data("+"))
but_add.place(x=365,y=190,height=70,width=115)






but_4=Button(win,text="4",font=("Times New Roman",20,"bold"),command=lambda:get_data(4))
but_4.place(x=20,y=260,height=70,width=115)

but_5=Button(win,text="5",font=("Times New Roman",20,"bold"),command=lambda:get_data(5))
but_5.place(x=135,y=260,height=70,width=115)

but_6=Button(win,text="6",font=("Times New Roman",20,"bold"),command=lambda:get_data(6))
but_6.place(x=250,y=260,height=70,width=115)

but_sub=Button(win,text="-",font=("Times New Roman",20,"bold"),command=lambda:get_data("-"))
but_sub.place(x=365,y=260,height=70,width=115)








but_7=Button(win,text="7",font=("Times New Roman",20,"bold"),command=lambda:get_data(7))
but_7.place(x=20,y=330,height=70,width=115)

but_8=Button(win,text="8",font=("Times New Roman",20,"bold"),command=lambda:get_data(8))
but_8.place(x=135,y=330,height=70,width=115)

but_9=Button(win,text="9",font=("Times New Roman",20,"bold"),command=lambda:get_data(9))
but_9.place(x=250,y=330,height=70,width=115)

but_mul=Button(win,text="*",font=("Times New Roman",20,"bold"),command=lambda:get_data("*"))
but_mul.place(x=365,y=330,height=70,width=115)







but_dot=Button(win,text=".",font=("Times New Roman",20,"bold"),command=lambda:get_data("."))
but_dot.place(x=250,y=400,height=70,width=115)


but_clear=Button(win,text="C",font=("Times New Roman",20,"bold"),command=clear)
but_clear.place(x=20,y=400,height=70,width=115)


but_0=Button(win,text="0",font=("Times New Roman",20,"bold"),command=lambda:get_data(0))
but_0.place(x=135,y=400,height=70,width=115)

but_div=Button(win,text="/",font=("Times New Roman",20,"bold"),command=lambda:get_data("/"))
but_div.place(x=365,y=400,height=70,width=115)


but_equal=Button(win,text="=",font=("Times New Roman",20,"bold"),command=equal_data)
but_equal.place(x=135,y=470,height=70,width=230)


win.mainloop()