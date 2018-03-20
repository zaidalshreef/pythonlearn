from tkinter import *
from tkinter import ttk

root=Tk()
def keyPressed(event):
    print("type {}".format(event.type))
    print("CTRL+C")
root.bind('<Control-c>',keyPressed)

bu = ttk.Button(root,text="click")
bu.pack()

def buttonPress(event):
    print("button is pressed")
bu.bind('<ButtonPress>',buttonPress)

root.mainloop()
