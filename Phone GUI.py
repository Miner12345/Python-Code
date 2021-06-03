import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect("phone.db")
#conn.execute("DROP TABLE PHONETABLE")
#conn.execute('''CREATE TABLE PHONETABLE (NAME TEXT NOT NULL,
                            #PHONENUMBER CHAR(20) NOT NULL);''')
def save():
    name=e1.get()
    phone=e2.get()
    if name=="":
        messagebox.showerror("Error","Name is required")
    elif phone=="":
        messagebox.showerror("Error","number is required")
    else:
        name=name.upper()
        query="SELECT NAME,PHONENUMBER FROM PHONETABLE WHERE NAME = '"+name+"'"
        cursor=conn.execute(query)
        data=cursor.fetchall()
        if len(data)!=0:
            messagebox.showerror("Error","Name is already existing can't insert")
        else:
            conn.execute("INSERT  INTO PHONETABLE(NAME,PHONENUMBER)VALUES(?,?)",(name,phone))
            messagebox.showinfo("Information","Successfully inserted"
def update():
  name=e1.get()
  name=name.upper()
  query="SELECT NAME,PHONENUMBER FROM PHONETABLE WHERE NAME = '"+name+"'"  
  cursor=conn.execute(query)
  data=cursor.fetchall()
  if len(data)==0:
    messagebox.showerror("Error","Name not found")
  else:
    phone=e2.get()
    if e2.get()=="":
      messagebox.showerror("Error","Phone number required")
    else:

      query="UPDATE PHONETABLE SET PHONENUMBER = '"+phone+"'WHERE NAME = '"+name+"'"
      
      conn.execute(query)
      messagebox.showinfo("Information","Successfully Updated")
def search():
  name=e1.get()
  
  if name=="":
    messagebox.showerror("Error","Must enter a phone number")
  else:
    name=name.upper()
    
    query="SELECT NAME,PHONENUMBER FROM PHONETABLE WHERE NAME ='"+name+"'"
    
    cursor=conn.execute(query)
    data=cursor.fetchall()
    if len(data)==0:
      messagebox.showerror("Error","Name not found")
    else:
      cursor=conn.execute(query)
      for row in cursor:
       e2.delete(0,END)
       e2.insert(0,row[1])
def delete():
    name=e1.get()
    name=name.upper()
    if name =="":
        message.showerror('Error','Must enter a name')
        
    else:
        query="SELECT NAME,PHONENUMBER FROM PHONETABLE WHERE NAME ='"+name+"'"
        cursor=conn.execute(query)
        data=cursor.fetchall()
        if len(data)==0:
            messagebox.showerror("Error","Name not found")
            
        else:
            query="DELETE FROM PHONETABLE WHERE NAME = '"+name+"'"
            conn.execute(query)
            messagebox.showinfo("Information","Successfully Deleted")
            e1.delete(0,END)
            e2.delete(0,END)

def close():
    answer=messagebox.askyesno("Confirm","Are you sure you want to exit")
    if answer==True:
        messagebox.showinfo("Information","Phone book v 1.0 created by Tarun")
        window.destroy()
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
window=tkinter.Tk()
window.geometry("500x400+100+100")
window.resizable(0,0)
l1=Label(window,text="Phone Book",font = "Times 15 bold")
l1.grid(row=0,column=1,padx=100)
l2=Label(window,text="Name",font = "Times 15 bold")
l2.grid(row=1,column=0)
e1=Entry(window,width=30)
e1.grid(row=1,column=1)
l3=Label(window,text="Number",font = "Times 15 bold")
l3.grid(row=2,column=0,pady=20)
e2=Entry(window,width=30)
e2.grid(row=2,column=1)
b1=Button(window,text="Save",font="Times 15 bold",command=save)
b1.grid(row=4,column=0)
b2=Button(window,text="Update",font="Times 15 bold",command=update)
b2.grid(row=4,column=1)
b3=Button(window,text="Search",font="Times 15 bold",command=search)
b3.grid(row=4,column=2)
b4=Button(window,text="Clear",font="Times 15 bold",padx=12,command=clear)
b4.grid(row=1,column=2)
b5=Button(window,text="Delete",font="Times 15 bold",command=delete)
b5.grid(row=2,column=2)
b6=Button(window,text="Exit",font="Times 15 bold",padx=12,command=close)
b6.grid(row=5,column=1,pady=10)


