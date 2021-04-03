from tkinter import *

def toplama():
    a=e1.get()
    b=e2.get()
    c=float(a)+float(b)
    print(c)
    answer.configure(text = str(c))
def cikarma():
    a=e1.get()
    b=e2.get()
    c=float(a)-float(b)
    print(c)
    answer.configure(text = str(c))
def carpma():
    a=e1.get()
    b=e2.get()
    c=float(a)*float(b)
    print(c)
    answer.configure(text = str(c))
def bolme():
    a=e1.get()
    b=e2.get()
    c=float(a)/float(b)
    print(c)
    answer.configure(text = str(c))

master= Tk()

Label(master, text="Enter a Number").grid(row=0)
Label(master, text="Enter a number").grid(row=2)
e1=Entry(master)
e1.grid(row=1)
e2=Entry(master)
e2.grid(row=3)

Button(master,text="*",command=carpma).grid(row=5,column=0,padx=5,pady=5)
Button(master,text="/",command=bolme).grid(row=5,column=1,padx=5,pady=5)
Button(master,text="+",command=toplama).grid(row=5,column=2,padx=5,pady=5)
Button(master,text="-",command=cikarma).grid(row=5,column=3,padx=5,pady=5)

answer=Label(master,text=" ")
answer.grid(row=6)
mainloop()
