import psycopg2
from tkinter import *
from PIL import Image, ImageTk
from addContact import *
from viewContact import *
from deleteContact import *
from retriveContact import *
from deleteContact import *
from updateContact import *

root = Tk()
root.minsize(width=400, height=400)
root.geometry('600x500')
root.title('Phone Book')
backgroundImage = Image.open(r'C:\Users\KEVIN\Desktop\GUI\Address Book\phoneBook.jpg')

perfect = TRUE
n = 1

[imageWidthSize, imageHeightSize] = backgroundImage.size

newImageWidth = int(imageWidthSize * n)
if perfect:
    newImageHeight = int(imageHeightSize * n)
else:
    newImageHeight = int(imageHeightSize / n)

# Inserting the Image
backgroundImage = backgroundImage.resize((newImageWidth, newImageHeight), Image.LANCZOS)
img = ImageTk.PhotoImage(backgroundImage)

canvas1 = Canvas(root)
canvas1.create_image(500, 300, image = img)
canvas1.config(bg= 'white',width=newImageWidth, height=newImageHeight )
canvas1.pack(expand=True, fill=BOTH)

# Head frame
frameL = Frame(root, bg ='#2c3e50', bd=1.5)
frameL.place(relx=0.3, rely=0.1, relwidth=0.6, relheight=0.13)
frameHead = Label(frameL, text='Kevin\'s Phonebook', font=('cambria', 20, 'italic'), bg='black', fg='white')
frameHead.place(relx=0, rely=0, relwidth=1, relheight=1)

# Buttons
btn1 = Button(root, text='Add Contact', font=('cambria', 15, 'italic'), bg='black', fg='white', command=Contact)
btn1.place(relx=0.38, rely= 0.3, relwidth=0.45, relheight=0.1)
btn2 = Button(root, text='Retrieve Contacts', font=('cambria', 15, 'italic'), bg='black', fg='white',
              command=retriveContacts)
btn2.place(relx=0.38, rely=0.4, relwidth=0.45, relheight=0.1)
btn3 = Button(root, text='View Contacts', font=('cambria', 15, 'italic'), bg='black', fg='white', command=View)
btn3.place(relx=0.38, rely=0.5, relwidth=0.45, relheight=0.1)
btn4 = Button(root, text='Update contacts', font=('cambria', 15, 'italic'), bg='black', fg='white',
              command=updateContacts)
btn4.place(relx=0.38, rely=0.6, relwidth=0.45, relheight=0.1)
btn5 = Button(root, text='Delete Contact', font=('cambria', 15, 'italic'), bg='black', fg='white',
              command=deleteContact)
btn5.place(relx=0.38, rely=0.7, relwidth=0.45, relheight=0.1 )


root.mainloop()