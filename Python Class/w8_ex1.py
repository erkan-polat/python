import tkinter as tk
root = tk.Tk()
logo = tk.PhotoImage(file="logo.gif")
w1 = tk.Label(root, image=logo).pack(side="right")
name="Besiktas"
w2 = tk.Label(root, 
 justify=tk.LEFT,
 padx = 10,
 text=name).pack(side="left")
root.mainloop()
