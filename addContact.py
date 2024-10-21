import psycopg2
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def contactRegister():
    phone = phonenumber.get()
    first = firstname.get()
    last = lastname.get()
    address = localaddress.get()

    try:
        cursor.execute("""INSERT INTO phonebook(firstname, lastname, phonenumber, address) 
        VALUES (%s,%s,%s,%s)""",(first, last, phone,address))
        con.commit()
        messagebox.showinfo("Success!!!", f"Added details for\n{first} {last} successfully!!")

    except:
        messagebox.showinfo("Error!!!", "Can\'t add data into the Database, check fields")

    print(f"{first}\n{last}\n{phone}\n{address}")
    root.destroy()


def Contact():
    global phonenumber, localaddress, firstname, lastname, cursor, con, root

    root = Tk()
    root.title('Add Book')
    root.minsize(width=400, height=400)
    root.geometry('720x500')

    con = psycopg2.connect(database='analysis',
                           host = 'localhost',
                           user = 'postgres',
                           password = 'Rosemary')
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS phonebook
                   (firstname text NOT NULL,
                   lastname text NOT NULL,
                   phonenumber text NOT NULL,
                   address text NOT NULL)""")
    con.commit()
    
    canvas1 = Canvas(root)
    canvas1.config(bg='#abb2b9')
    canvas1.pack(expand=True, fill=BOTH)

    labeFrame = Frame(root, bg='#fad7a0', bd=1.2)
    labeFrame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    labF = Label(labeFrame, text="Add Contact", fg='white', bg='black', font=('cambria', 20, 'bold'))
    labF.place(relx=0, rely=0, relwidth=1, relheight=1)

    contactFrame = Frame(root, bg='black')
    contactFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    contactfirst = Label(contactFrame, text='First Name: ', fg='white', bg='black', font=('cambria', 15))
    contactfirst.place(relx=0.05, rely=0.2, relheight=0.08)
    firstname = Entry(contactFrame, font=('cambria', 15))
    firstname.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.1)

    contactLast = Label(contactFrame, text='Last Name: ', fg='white', bg='black', font=('cambria', 15))
    contactLast.place(relx=0.05, rely=0.35, relheight=0.08)
    lastname = Entry(contactFrame, font=('cambria', 15))
    lastname.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.1)

    contactPhone = Label(contactFrame, text='Phone Number: ', fg='white', bg='black', font=('cambria', 15))
    contactPhone.place(relx=0.05, rely=0.50, relheight=0.09)
    phonenumber = Entry(contactFrame,font=('cambria', 15))
    phonenumber.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.1)

    contactA = Label(contactFrame, text='Address: ', fg='white', bg='black', font=('cambria', 15))
    contactA.place(relx=0.05, rely=0.65, relheight=0.08)
    localaddress = Entry(contactFrame, font=('cambria', 15))
    localaddress.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.1)
    submitbtn = Button(root, text='Add contact', bg = '#D1CCC0', fg='black', command=contactRegister, font=('cambria', 12, 'bold'),)
    submitbtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text='Quit', bg='#F7F1E3', fg='black', command=root.destroy, font=('cambria', 12, 'bold'))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)


    root.mainloop()
