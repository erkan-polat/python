from tkinter import *

def show_matrice():
    b=w1.get()
    a=w2.get()
    for i in range(0,b+4):
        if((i%2)==0):
            print(a*'.-'+'.')
        else:
            print(a*'| '+'|')

master = Tk()
w1=Scale(master, from_=0, to=10)
w1.pack()
w2=Scale(master, from_=0, to=10, orient=HORIZONTAL)
w2.pack()
Button(master, text='Show', command=show_matrice).pack()

mainloop()
