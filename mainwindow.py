from tkinter import *

class DataEntry():
    def __init__(self,rootone):
        self.rootone = rootone

    def bill_window(self):
        import billtable

    def employee_window(self):
        import employeetable

        




root = Tk()
a = DataEntry(root)
root.title("Multiple windows")

root.geometry("560x360+120+120")

label1=Label(text="THIS IS MAIN WINDOW",fg="green")
label1.pack()


#menu section
mymenu = Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="tables",menu=submenu)
submenu.add_command(label="demotable",command="")
submenu.add_separator()
submenu.add_command(label="employee",command=a.employee_window)
submenu.add_separator()
submenu.add_command(label="bill",command=a.bill_window)








root.mainloop()