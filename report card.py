from tkinter import *
from tkinter.messagebox import askokcancel





def get_data():
    name=st_name_1.get()

    hindi=hindi_name_1.get()
    english=english_name_1.get()
    math=math_name_1.get()
    science=science_name_1.get()

    total=hindi+english+math+science
    per=(total/400)*100

    div=""
    

    if per>=60:
        div="1st divison"
    elif per<60 and per>=50:
        div="2nd divison"
    elif per<50 and per>=33:
        div="3rd divison"

    else:
        div="Fail"

    message_box(name,total,per,div)



def message_box(*data):
    print_1=f""" 
    Name : {data[0]}
    total : {data[1]}
    percentage : {data[2]}
    division : {data[3]}
    """
    askokcancel(title="Report",message=print_1)





win=Tk()
win.title("Progress report")
win.config(bg="white")
#win.iconbitmap("")
win.geometry("600x690")
win.resizable(False,False)


school_name=Label(win,text="School Report",font=("Times New Roman",40,"bold"),bg="white")
school_name.place(x=70,y=50)

st_name=Label(win,text="Student Name",font=("Times New Roman",20,"bold"))
st_name.place(x=70,y=180)


st_name_1=StringVar()
st_name_entry=Entry(win,font=("Times New Roman",20,"bold"),textvariable=st_name_1)
st_name_entry.place(x=270,y=180 )

sub_name=Label(win,text="Subject Number",font=("Times New Roman",20,"bold"))
sub_name.place(x=150,y=240,width=300)


#l=["Odia","English","Math","Science"]

hindi_name_1=DoubleVar()
english_name_1=DoubleVar()
math_name_1=DoubleVar()
science_name_1=DoubleVar()





hindi_name=Label(win,text="Hindi",font=("Times New Roman",20,"bold"))
hindi_name.place(x=70,y=300)
hindi_name_entry=Entry(win,font=("Times New Roman",20,"bold"),textvariable=hindi_name_1)
hindi_name_entry.place(x=270,y=300)



english_name=Label(win,text="English",font=("Times New Roman",20,"bold"))
english_name.place(x=70,y=370)
english_name_entry=Entry(win,font=("Times New Roman",20,"bold"),textvariable=english_name_1)
english_name_entry.place(x=270,y=370)


science_name=Label(win,text="Science",font=("Times New Roman",20,"bold"))
science_name.place(x=70,y=440)
science_name_entry=Entry(win,font=("Times New Roman",20,"bold"),textvariable=science_name_1)
science_name_entry.place(x=270,y=440)


math_name=Label(win,text="Math",font=("Times New Roman",20,"bold"))
math_name.place(x=70,y=510)
math_name_entry=Entry(win,font=("Times New Roman",20,"bold"),textvariable=math_name_1)
math_name_entry.place(x=270,y=510)


button=Button(win,text="Done",font=("Times New Roman",20,"bold"),command=get_data)
button.place(x=200,y=550,width=150,height=40)

win.mainloop()