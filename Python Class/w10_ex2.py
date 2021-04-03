from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def open_file():
    name = filedialog.askopenfilename()
    f = open(name,'r')
    text=f.read()
    print(text)
    e1.insert(END,text)
    f.close()
def save_file():
    f=open("labexample.txt",'w')
    text=e1.get("1.0",END)
    f.write(text)
    f.close()
def callback():
    print("exit")
    if messagebox.askyesno('Verify','Really quit?'):
        print("Yes")
        root.destroy()
    else:
        print("No")

root = Tk()

##create menu bar
menubar = Menu(root)
##file menu
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command = open_file)
filemenu.add_command(label="Save",command = save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit",command = callback)
e1 = Text(root,height = 20,width = 50)
e1.pack()

root.config(menu = menubar)
mainloop()
