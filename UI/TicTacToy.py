from  tkinter import *
from tkinter import ttk
from tkinter import messagebox
from  random import  randint

activeplayer=1 #set active player
p1=[]
p2=[]

root=Tk()
root.title(" Tic Tac Toy : player 1")
style=ttk.Style()
style.theme_use("classic")

bu1=ttk.Button(root,text="")
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda :buclick(1))
bu2=ttk.Button(root,text="")
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda :buclick(2))
bu3=ttk.Button(root,text="")
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda :buclick(3))
bu4=ttk.Button(root,text="")
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda :buclick(4))
bu5=ttk.Button(root,text="")
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda :buclick(5))
bu6=ttk.Button(root,text="")
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda :buclick(6))
bu7=ttk.Button(root,text="")
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda :buclick(7))
bu8=ttk.Button(root,text="")
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda :buclick(8))
bu9=ttk.Button(root,text="")
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda :buclick(9))

def setlayot(id, text):
    if(id==1):
        bu1.config(text=text)
        bu1.state(['disabled'])
    elif(id==2):
        bu2.config(text=text)
        bu2.state(['disabled'])
    elif(id==3):
        bu3.config(text=text)
        bu3.state(['disabled'])
    elif(id==4):
        bu4.config(text=text)
        bu4.state(['disabled'])
    elif(id==5):
        bu5.config(text=text)
        bu5.state(['disabled'])
    elif(id==6):
        bu6.config(text=text)
        bu6.state(['disabled'])
    elif(id==7):
        bu7.config(text=text)
        bu7.state(['disabled'])
    elif(id==8):
        bu8.config(text=text)
        bu8.state(['disabled'])
    elif(id==9):
        bu9.config(text=text)
        bu9.state(['disabled'])

def checkwiner():
    win=0
    if((1 in p1) and (2 in p1) and (3 in p1) ):
        win=1
    if((4 in p1) and (5 in p1) and (6 in p1)):
        win=1
    if((7 in p1) and (8 in p1) and (9 in p1)):
        win=1
    if((1 in p1) and (4 in p1) and (7 in p1)):
        win=1
    if((2 in p1) and (5 in p1) and (8 in p1)):
        win=1
    if((3 in p1) and (6 in p1) and (9 in p1)):
        win=1
    if((3 in p1) and (5 in p1) and (7 in p1)):
        win=1
    if((1 in p1) and (5 in p1) and (9 in p1)):
        win=1
    #player 2
    if((1 in p2) and (2 in p2) and (3 in p2) ):
        win=2
    if((4 in p2) and (5 in p2) and (6 in p2)):
        win=2
    if((7 in p2) and (8 in p2) and (9 in p2)):
        win=2
    if((1 in p2) and (4 in p2) and (7 in p2)):
        win=2
    if((2 in p2) and (5 in p2) and (8 in p2)):
        win=2
    if((3 in p2) and (6 in p2) and (9 in p2)):
        win=2
    if((3 in p2) and (5 in p2) and (7 in p2)):
        win=2
    if((1 in p2) and (5 in p2) and (9 in p2)):
        win=2
    if(win==1):
        messagebox.showinfo(title="player 1",message="Player 1 win")
        root.quit()
    elif(win==2):
        messagebox.showinfo(title="player 2", message="Player 2 win")
        root.quit()

def AI():
    global  p1
    global  p2
    empty=[]
    for cell in range(9):
        if(not((cell+1 in p1) or (cell+1 in p2))):
            empty.append(cell+1)
    if(len(empty)>=1):
        RandIndex=randint(0,len(empty)-1)
        buclick(empty[RandIndex])

def buclick(id):
    global activeplayer
    global p1
    global p2
    if(activeplayer==1):
        setlayot(id,'X')
        p1.append(id)
        root.title(" Tic Tac Toy : player 2")
        activeplayer=2
        print("p1:{}".format(p1))
        AI()
    elif(activeplayer==2):
        setlayot(id, 'Y')
        p2.append(id)
        root.title(" Tic Tac Toy : player 1")
        activeplayer = 1
        print("p2:{}".format(p2))
    checkwiner()

root.mainloop()