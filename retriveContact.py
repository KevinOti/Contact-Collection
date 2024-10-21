from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import psycopg2


def enterFirstName():
    y = 0.35
    first_name = name.get()
    con = psycopg2.connect(dbname ='analysis',
                           host = 'localhost', user ='postgres', password = 'Rosemary')
    cur = con.cursor()

    try:
        cur.execute("""SELECT * FROM phonebook WHERE firstname ILIKE '{}%' """.format(first_name))
        books = cur.fetchall()
        
        for i in books:
            Label(frameD, text="{}\t\t {}\t\t   {}\t\t{}".format(i[0].title(), i[1].title(), i[2], i[3].title()), fg='white', 
                  bg='black', font=('cambria', 13)).place(relx=0.07, rely=y)
            y += 0.1

    except:
        messagebox.showinfo("No such name in the database")
        print(first_name)


def retriveContacts():
    global name, root, frameD, first_name
    root = Tk()
    root.minsize(width=400, height=400)
    root.title("Retrive Contacts")
    root.geometry('750x500')
    canvas1 = Canvas(root)
    canvas1.config(bg='#21618c')
    canvas1.pack(expand=True, fill=BOTH)

    frame1 = Frame(root, bg='#fcf3cf', bd=1.2)
    frame1.place(relx=0.2, rely=0.03, relwidth=0.6, relheight=0.1)
    frame2 = Label(frame1, text='Retrive Contacts', font=('cambria', 20, 'bold'),fg='white', bg='black')
    frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameD = Frame(root, bg='black')
    frameD.place(relx=0.1, rely=0.15, relwidth=0.85, relheight=0.8)
    frameE = Label(frameD, text="Contact Name: ", font=('cambria', 15), fg='white', bg='black')
    frameE.place(relx=0.05, rely=0.1)
    name = Entry(frameD)
    name.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.075)

    frameLine = Label(frameD, text="{}\t {}\t {}\t  {}".format('First Name', 'Last Name', 'Phone Number', "Address"),
                      fg='white', bg='black', font=('cambria', 13, 'bold'))
    frameLine.place(relx=0.05, rely=0.25)
    frameLine2 = Label(frameD, text=f"{'-'*120}", fg='white', bg='black')
    frameLine2.place(relx=0.05, rely=0.3)

    submitButton = Button(root, text="Submit", bg='#D1CCC0', fg='black', font=('cambria', 15, 'bold'),
                          command=enterFirstName)
    
    submitButton.place(relx=0.28, rely=0.86, relwidth=0.17, relheight=0.07)
    quitButton = Button(root, text="Quit", bg="#F7F1E3", fg='black', command=root.destroy, font=('cambria', 15, 'bold'))
    quitButton.place(relx=0.53, rely=0.86, relwidth=0.17, relheight=0.07)



    root.mainloop()



