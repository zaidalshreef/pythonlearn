from tkinter import *
from tkinter import ttk
from databaseConnect import DBConnect


class ListTicket:

    def __init__(self):
       self.root=Tk()
       self.DBC=DBConnect()
       tv=ttk.Treeview(self.root)
       tv.pack()
       tv.heading('#0',text='ID')
       tv.configure(column=('#Name','#Gender','#Comment'))
       tv.heading('#Name',text='Name')
       tv.heading('#Gender',text='Gender')
       tv.heading('#Comment',text='Comment')
       cursor=self.DBC.ListRequst()
       for row in cursor:
           tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
           tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
           tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
           tv.set('#{}'.format(row['ID']),'#Comment',row['Comment'])

       self.root.mainloop()
