from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Calculator")
window.geometry('550x310')
l1=Label(window,text="Enter the first value: ")
l1.grid(column=1,row=1,padx=10,pady=10,sticky="W")
e1=Entry(window,width=20)
e1.grid(column=2,row=1,padx=10,pady=10)

l2=Label(window,text="Enter the second value: ")
l2.grid(column=1,row=2,padx=10,pady=10,sticky="W")
e2=Entry(window,width=20)
e2.grid(column=2,row=2,padx=10,pady=10)


def add():
    res=int(e1.get())+int(e2.get())
    l4.configure(text=res)

def subtract():
    res=int(e1.get())-int(e2.get())
    l4.configure(text=res)
def multiple():
    res=int(e1.get())*int(e2.get())
    l4.configure(text=res)

def divide():
    res=int(e1.get())/int(e2.get())
    l4.configure(text=res)





bt1=Button(window,text="Add",command=add)
bt1.grid(column=4,row=1,padx=10,pady=10)
bt2=Button(window,text="Subtract",command=subtract)
bt2.grid(column=5,row=1,padx=10,pady=10)
bt3=Button(window,text="Multiple",command=multiple)
bt3.grid(column=4,row=2,padx=10,pady=10)
bt4=Button(window,text="Divide",command=divide)
bt4.grid(column=5,row=2,padx=10,pady=10)

l3=Label(window,text="Result: ")
l3.grid(column=1,row=6,padx=10,pady=10,sticky="W")

l4=Label(window,text="")
l4.grid(column=2,row=6,padx=10,pady=10,sticky="W")

window.mainloop()