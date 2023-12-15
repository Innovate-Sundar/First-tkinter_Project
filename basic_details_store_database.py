from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id=e_id.get();
    name=e_name.get();
    phone=e_phone.get();

    if(id==""or name==""or phone==""):
        MessageBox.showinfo("Insertion Status","all required")
    else:
        con=mysql.connect(host='localhost',user='xxxx',passwd='xxxx',port='3306',database='xxxx')
        cursor=con.cursor()
        cursor.execute("insert into details values('"+id+"','"+name+"','"+phone+"')")
        cursor.execute("commit")
        cursor=MessageBox.showinfo("Insert Status","Insertion Completed Successfully!")
        con.close()

root=Tk()

id=Label(root,text='Enter Id',font=('Bold',10))
id.place(x=40,y=60)

name=Label(root,text='Enter Name',font=('Bold',10))
name.place(x=40,y=120)

phone=Label(root,text='Enter Phone',font=('Bold',10))
phone.place(x=40,y=180)

e_id=Entry()
e_id.place(x=120,y=60)

e_name=Entry()
e_name.place(x=120,y=120)

e_phone=Entry()
e_phone.place(x=120,y=180)

insert=Button(root,text='Insert',font='Italic',bg='White',command=insert)
insert.place(x=120,y=240)

root.mainloop()