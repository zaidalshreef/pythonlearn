from  tkinter import *
from tkinter import ttk

root=Tk()
style=ttk.Style()
style.theme_use("classic")
ttk.Label(root,background="Green",text="Green").grid(row=0,column=0,sticky='snew',ipadx=10,ipady=10)
ttk.Label(root,background="Yellow",text="Yellow").grid(row=0,column=1,sticky='snew')
ttk.Label(root,background="Blue",text="Blue").grid(row=1,column=0,columnspan=2,sticky='snew')
ttk.Label(root,background="Orange",text="Orange").grid(row=0,column=2,rowspan=2,sticky='snew')
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=2)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)




root.mainloop()