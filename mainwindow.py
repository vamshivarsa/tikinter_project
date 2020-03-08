from tkinter import *


def bill_window():
        import billtable
            
def employee_window():
        import employeetable



root = Tk()
root.title("Multiple windows")
root.geometry("560x360+120+120")

canvas = Canvas(root,width=560,height=360)
canvas.pack()

image1= PhotoImage(file="pydatabase.PNG")
canvas.create_image(0,0,image=image1,anchor=NW)

label1=Label(canvas,text="THIS IS MAIN WINDOW",fg="green")
label1.place()

#menu section
mymenu = Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="tables",menu=submenu)
submenu.add_command(label="demotable",command="")
submenu.add_separator()
submenu.add_command(label="employee",command=lambda :employee_window())
submenu.add_separator()
submenu.add_command(label="bill",command=lambda:bill_window())

root.mainloop()