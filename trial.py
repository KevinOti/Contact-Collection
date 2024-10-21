import psycopg2
from tkinter import messagebox
conn = psycopg2.connect(database='analysis',
                        user = 'postgres',
                        host = 'localhost',
                        password = 'Rosemary')

cur = conn.cursor()

contact_change = '00000000'
first = 'Peter'
last = 'andreas'
addr = 'Kiambu'
try:
    cur.execute("""UPDATE phonebook 
                SET firstname = '{}', lastname='{}',address = '{}'
                WHERE phonenumber = '{}'""".format(first, last, addr, contact_change))
    conn.commit()
    messagebox.showinfo("success", 
                            f"Update details to\n{first.title()} {last.title()}\nSuccessfully")
except:
    messagebox.showinfo("Wrong details provided")

cur.execute("""SELECT * FROM phonebook""")
data = cur.fetchall()
for a in data:
    print(a)