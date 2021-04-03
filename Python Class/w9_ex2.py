from tkinter import *

master = Tk()

w= Canvas(master, width=1000,height=1000)

w.pack()

w.create_oval(150,150,350,350,fill='yellow',outline='yellow')
w.create_line(250,400,250,500,fill='yellow',width=3)
w.create_line(400,250,500,250,fill='yellow',width=3)
w.create_line(250,100,250,0,fill='yellow',width=3)
w.create_line(100,250,0,250,fill='yellow',width=3)
w.create_line(350,375,450,450,fill='yellow',width=3)
w.create_line(50,50,150,150,fill='yellow',width=3)
ev=[300,1000,500,1000,500,800,300,800]
kapi=[400,1000,450,1000,450,900,400,900]
pencere=[325,950,375,950,375,900,325,900]
cati=[275,800,525,800,400,600]
agac=[800,1000,850,1000,850,800,900,800,825,700,750,800,800,800,]
dal=[750,700,900,700,825,600]
w.create_polygon(ev,outline='blue',fill='blue')
w.create_polygon(kapi,outline='white',fill='white')
w.create_polygon(kapi,outline='white',fill='white')
w.create_polygon(pencere,outline='white',fill='white')
w.create_polygon(cati,outline='red',fill='red')
w.create_polygon(agac,outline='green',fill='green')
w.create_polygon(dal,outline='green',fill='green')
mainloop()
