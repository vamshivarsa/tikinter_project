from tkinter import *

class DataEntry():
    def __init__(self,rootone):
        self.rootone = rootone

    def open_window(self):
        self.rootone.destroy()
        import app

        




root = Tk()
a = DataEntry(root)
root.title("Multiple windows")

root.geometry("560x360+120+120")


#menu section
mymenu = Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="tables",menu=submenu)
submenu.add_command(label="demotable",command=a.open_window)
submenu.add_separator()
submenu.add_command(label="employee",command=a.open_window)
submenu.add_separator()
submenu.add_command(label="bill",command=a.open_window)








root.mainloop()