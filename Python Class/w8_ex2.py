import tkinter as tk

root =tk.Tk()

v=tk.IntVar()

lst=["","Besiktas","Fenerbahce","Galatasaray","Trabzonspor"]

def save_team():
    team=v.get()
    f=open("teamdata.txt",'w')
    f.write(lst[team])
    f.close()

tk.Radiobutton(root,text="Besiktas",variable=v,value=1,command=save_team).pack()
tk.Radiobutton(root,text="Fenerbahce",variable=v,value=2,command=save_team).pack()
tk.Radiobutton(root,text="Galatasaray",variable=v,value=3,command=save_team).pack()
tk.Radiobutton(root,text="Trabzonspor",variable=v,value=4,command=save_team).pack()


root.mainloop()
