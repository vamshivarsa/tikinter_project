from tkinter import *
import psycopg2

def submit():
    conn=psycopg2.connect(dbname="vamshi",user="postgres",password="davs",host="localhost",port="5432")
    cur = conn.cursor()
    name1 = namebox.get()
    company1=companybox.get()
    salary1=salarybox.get()
    query='''insert into employee(name,company,salary) values(%s,%s,%s); '''
    cur.execute(query,(name1,company1,salary1))
    print("data inserted successfully in bill table")
    conn.commit()
    conn.close()


root = Tk()
root.title("DATA ENTRY FORM")
root.geometry("560x360+120+120")


#adding canvas

canvas=Canvas(root,width=400,height=400)
canvas.pack()

frame = Frame(root)
frame.place(relx=0.3, rely=0.3,relwidth=0.8,relheight=0.8)

#adding column name lables

name = Label(frame,text="Name : ")
name.grid(row=0,column=2)

comapany = Label(frame,text="company : ")
comapany.grid(row=1,column=2)

salary = Label(frame,text="salary : ")
salary.grid(row=2,column=2)


# addiing entry boxes for respective columns

namebox = Entry(frame)
namebox.grid(row=0,column=3)


companybox = Entry(frame)
companybox.grid(row=1,column=3)

salarybox = Entry(frame)
salarybox.grid(row=2,column=3)

#adding buttons
insertbutton = Button(frame,text="insert",bd=6,command=submit)
insertbutton.grid(row=4,column=3)

root.mainloop()