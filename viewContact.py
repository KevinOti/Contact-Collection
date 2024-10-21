from tkinter import *
import psycopg2
from PIL import Image, ImageTk
from tkinter import messagebox

con = psycopg2.connect(database='analysis',
                       host = 'localhost',
                       user = 'postgres',
                       password = 'Rosemary')
cur = con.cursor()

def View():
    root = Tk()
    root.minsize(width=400, height=400)
    root.geometry('800x500')
    root.title('View Contacts')

    canvas1 = Canvas(root)
    canvas1.config(bg="#d2b4de")
    canvas1.pack(expand=True, fill=BOTH)

    headFrame = Frame(root, bg="#f9e79f", bd=1.3)
    headFrame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headL = Label(headFrame, text="Contacts", font=('cambria', 20, 'bold'), fg='white', bg='black')
    headL.place(relx=0, rely=0, relwidth=1, relheight=1)

    detailFrame = Frame(root, bg='black')
    detailFrame.place(relx=0.06, rely=0.3, relwidth=0.9, relheight=0.5)
    y = 0.25

    Label(detailFrame, text="{}\t{}\t {}\t\t{}".format('First Name', 'Last Name', 'Phone Number', 'Address'),
                    fg='white', bg='black', font=('cambria', 13, 'bold')).place(relx=0.07, rely=0.1)
    Label(detailFrame, text=f'{"-"*130}', bg='black', fg='white').place(relx=0.07, rely=0.2,)
    

    try:
        cur.execute("""SELECT * FROM phonebook LIMIT 8""")
        rows = cur.fetchall()
        for i in rows:
            Label(detailFrame, text="{}\t\t   {}\t\t        {}\t\t\t{}".format(i[0].title(), i[1].title(), i[2].strip(), i[3].title().strip()), 
                  fg='white', bg='black', font=('cambria', 12)).place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to retrive data")


    root.mainloop()





