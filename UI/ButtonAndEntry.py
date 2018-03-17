from tkinter import *
from tkinter import ttk

root=Tk()

entry=ttk.Entry(root,width=40)
entry.pack()

login=PhotoImage(file='login.gif')
resize = login.subsample(2,10)
bu1=ttk.Button(root,text="get text")
bu1.pack()
bu1.config(image=resize,compound=CENTER)


def buclick():
    print(entry.get())
    entry.delete(0,END)

bu1.config(command=buclick)



root.mainloop()
