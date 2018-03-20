from  tkinter import *
from tkinter import ttk

root=Tk()

bu1=ttk.Button(root,text="Click me 1")
bu1.pack()
bu2=ttk.Button(root,text="Click me 2")
bu2.pack()
bu3=ttk.Button(root,text="Click me 3")
bu3.pack()


def buclick(x):
    print("Clicked {}".format(x))

bu1.config(command= lambda : buclick(1))
bu2.config(command= lambda : buclick(2))
bu3.config(command= lambda : buclick(3))



root.mainloop()
