from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import psycopg2

def delete():
    number =phonenumber.get()
    conn = psycopg2.connect(database='analysis',
                            host = 'localhost',
                            user = 'postgres',
                            password = 'Rosemary')
    cur = conn.cursor()

    try:
        cur.execute("""DELETE FROM phonebook WHERE phonenumber = '{}'""".format(number) )
        conn.commit()
        messagebox.showinfo("Success!!",f"\nDetails for {number} deleted successfully")
    except:
        messagebox.showinfo("Check the number")
    
    print(number)

def deleteContact():
    global phonenumber
    root = Tk()
    root.minsize(width=400, height=400)
    root.geometry('600x500')
    root.title('Delete Contact')

    canvas1 = Canvas()
    canvas1.config(bg='#0e6655')
    canvas1.pack(expand=True, fill=BOTH)

    frameHead = Frame(root, bg = '#f9e79f', bd=1.3)
    frameHead.place(relx=0.2, rely=0.1, relheight=0.16, relwidth=0.6)

    frameD = Label(frameHead, text="Delete Contact", font=('cambria', 20, 'bold'),
                   bg = 'black', fg='white')
    frameD.place(relx=0, rely=0, relwidth=1, relheight=1)

    frameC = Frame(root, bg='black')
    frameC.place(relx=0.1, rely=0.3, relwidth=0.85, relheight=0.5)

    Label(frameC, text="Phone Number: ", font=('cambria', 12), 
          bg='black', fg='white').place(relx=0.05, rely=0.5)
    phonenumber = Entry(frameC, font=('cambria', 15))
    phonenumber.place(relx=0.3, rely=0.5, relwidth=0.62)

    Button(root, text="Submit", bg="#D1CCC0", fg="black",command=delete,
           font=('cambria', 12, 'bold')).place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    Button(root, text='Quit', bg='#F7F1E3', fg='black',
           font=('cambria', 12, 'bold'),
           command=root.destroy).place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)






    root.mainloop()


