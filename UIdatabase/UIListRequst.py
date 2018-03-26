from tkinter import *
from tkinter import ttk
from databaseConnect import DBConnect


class ListTicket:


    def __init__(self):
       def delete():
           id=self.tv.selection()[0]
           ID=int(id[1])
           self.DBC.deleteRecord(ID)
           self.root.destroy()
       def Update():
           def up():
             self.DBC.UpdateRecord(ID,coment.get(1.0,'end'))
             self.root.destroy()


           id=self.tv.selection()[0]
           ID=int(id[1])
           ttk.Label(self.root, text='Coment :').grid(row=2, column=0, padx=10, pady=10)
           coment = Text(self.root)
           coment.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
           b1=ttk.Button(self.root,text='submit')
           b1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
           b1.config(command=up)


       self.root=Tk()
       self.DBC=DBConnect()
       self.tv=ttk.Treeview(self.root)
       self.tv.grid(row=0,column=0,columnspan=2)
       self.tv.heading('#0',text='ID')
       self.tv.configure(column=('#Name','#Gender','#Comment'))
       self.tv.heading('#Name',text='Name')
       self.tv.heading('#Gender',text='Gender')
       self.tv.heading('#Comment',text='Comment')
       self.b1=ttk.Button(self.root,text='delete')
       self.b1.grid(row=1,column=0,padx=10,pady=10)
       self.b1.config(command=delete)
       self.b2 =ttk.Button(self.root, text='update')
       self.b2.grid(row=1, column=1)
       self.b2.config(command=Update)

       cursor=self.DBC.ListRequst()
       for row in cursor:
           self.tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
           self.tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
           self.tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
           self.tv.set('#{}'.format(row['ID']),'#Comment',row['Comment'])

       self.root.mainloop()



