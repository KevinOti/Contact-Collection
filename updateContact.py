from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import psycopg2
conn = psycopg2.connect(database = 'analysis',
                        host = 'localhost',
                        user = 'postgres',
                        password = 'Rosemary')
cur = conn.cursor()

def contactList():
    new_list = []
    cur.execute("""SELECT phonenumber FROM phonebook""")
    details = cur.fetchall()
    for det in details:
        new_list.append(det[0])
    return new_list
contactlist = contactList()

def Update():
    contact_change = contact.get()
    first = firstname.get()
    last = lastname.get()
    addr = address.get()
    try:
        cur.execute("""UPDATE phonebook 
                    SET firstname = '{}', lastname='{}',address = '{}'
                    WHERE phonenumber = '{}'""".format(first, last, addr, contact_change))
        conn.commit()
        messagebox.showinfo("success", 
                            f"Update details to\n{first.title()} {last.title()}\nSuccessfully")
    except:
        messagebox.showinfo("Wrong details provided")

def updateContacts():
    global conn, cur, contact, contactlist, firstname, lastname, address

    root = Tk()
    root.minsize(width=400, height=400)
    root.geometry('700x500')
    root.title("Update Contact")

    canvas1 = Canvas(root)
    canvas1.config(bg='grey')
    canvas1.pack(expand=True, fill=BOTH)

    frame1 = Frame(root, bg='#FFEE00', bd=1.2)
    frame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.13)
    frameU = Label(frame1, text="Update Contact", font=('cambria', 15, 'bold'), fg='white',
                   bg='black')
    frameU.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameE = Frame(root, bg='black')
    frameE.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    frameContact =Label(frameE, text="Select Contact", fg='white', bg='black',
                        font=('cambria', 15))
    frameContact.place(relx=0.05, rely=0.1, relheight=0.1)
    contact = ttk.Combobox(frameE, values=contactlist, 
                           font=('cambria', 12), state='readonly')
    contact.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.1)
    
    firstn =Label(frameE, text="First Name", font=('cambria', 12), fg='white',
                  bg='black')
    firstn.place(relx=0.05, rely=0.3, relheight=0.1)
    firstname =Entry(frameE)
    firstname.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.1)
    
    lastn = Label(frameE, text="Last Name", font=('cambria', 15), fg='white',
                  bg='black')
    lastn.place(relx=0.05, rely=0.5, relheight=0.1)
    lastname = Entry(frameE)
    lastname.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.1)

    addres = Label(frameE, text="Address", font=('cambria', 15), fg='white', bg='black')
    addres.place(relx=0.05, rely=0.7, relheight=0.1)
    address = Entry(frameE)
    address.place(relx=0.3, rely=0.7, relwidth=0.62, relheight=0.1)

    Button(root, text="Submit", bg = '#D1CCC0', fg='black', command=Update, font=('cambria', 12, 'bold')).place(
        relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    Button(root, text="Quit", bg = '#D1CCC0', fg='black', command=root.destroy, font=('cambria', 12, 'bold')).place(
        relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


