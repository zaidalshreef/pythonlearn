from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from databaseConnect import DBConnect
from  UIListRequst import ListTicket

dbConnect=DBConnect()
root=Tk()
root.configure(background="#e1d8b2")
style=ttk.Style(root)
print(style.theme_names())
style.theme_use('classic')
style.configure('Tlabel',background="#e1d8b2")
style.configure('TButton',background="#e1d8b2")
style.configure('TRadiobutton',background="#e1d8b2")
root.title("Ticket reservation")
#full name
ttk.Label(root,text="full name :").grid(row=0,column=0,padx=10,pady=10)
fullname=ttk.Entry(root,width=40,font=('Arial',16))
fullname.grid(row=0,column=1,columnspan=2,padx=10,pady=10)
#gender
ttk.Label(root,text='Gender :').grid(row=1,column=0,padx=10,pady=10)
gender=StringVar()
RB1=ttk.Radiobutton(root,text='male',variable=gender,value='male').grid(row=1,column=1,padx=10,pady=10)
RB2=ttk.Radiobutton(root,text='female',variable=gender,value='female').grid(row=1,column=2,padx=10,pady=10)
#coment
ttk.Label(root,text='Coment :').grid(row=2,column=0,padx=10,pady=10)
coment=Text(root)
coment.grid(row=2,column=1,columnspan=2,padx=10,pady=10)

#buttons
buSubmit=ttk.Button(root,text='submit')
buSubmit.grid(row=3,column=3,padx=10,pady=10)
buIist=ttk.Button(root,text='listReq')
buIist.grid(row=3,column=2,padx=10,pady=10)

def BuSubmit():
    print("Full name: {}".format(fullname.get()))
    print(" gender: {}".format(gender.get()))
    print(" comment : {}".format(coment.get(1.0,'end')))
    print(coment.get(1.0,'end'))
    mag=dbConnect.add(fullname.get(),gender.get(),coment.get(1.0,'end'))
    messagebox.showinfo(title='info',message=mag)
    fullname.delete(0,'end')
    coment.delete(1.0,'end')

def Bulist():
    list=ListTicket()


buSubmit.config(command=BuSubmit)
buIist.config(command=Bulist)
root.mainloop()
