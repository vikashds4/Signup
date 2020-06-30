"""Sign Up"""

from tkinter import *
import tkinter.font as font
import re
import sqlite3
from tkinter import messagebox

# Regular expression for database entities
regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_userid = '(?i)^(?=.*[a-z])[a-z0-9]{8,20}$'
regex_password = '^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@$%]){8,32}'


def get_data():
    full_name = text1.get()
    email_id = text2.get()
    user_id = text3.get()
    password = text4.get()
    c_password = text5.get()
    list = validation(full_name, email_id, user_id, password, c_password)
    return list


def send_data():
    db = sqlite3.connect('shadow.db')
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists User(name text,email text,user text,password text)")
    list2 = get_data()
    if list2:
        db.execute("insert into User(name ,email,user,password) values (?,?,?,?)",
                   (list2[0], list2[1], list2[2], list2[3]))
        messagebox.showinfo('Success', 'Ok')
    db.commit()


def validation(name, email, user, fpass, cpass):
    flag = True
    if name is "":
        wr1.config(text='Name can not be empty')
        flag = FALSE
    else:
        wr1.config(text='')
        val_name = name
    if email is '':
        wr2.config(text='Email can not be empty')
        flag = FALSE
    elif re.search(regex_email, email):
        val_email = email
        wr2.config(text='')
    else:
        wr2.config(text='Invalid email')
        flag = FALSE
    if user is '':
        wr3.config(text='Username can not be empty')
        flag = FALSE
    elif user and re.search(regex_userid, user) and not re.search("[A-Z]", user):
        val_user = user
        wr3.config(text='')
    else:
        wr3.config(text='Invalid username')
        flag = FALSE
    if fpass is '':
        wr4.config(text='Password can not be empty')
        flag = FALSE
    elif re.search(regex_password, fpass):
        val_fpass = fpass
        wr4.config(text='')
    else:
        wr4.config(text='Invalid password')
        flag = FALSE
    if cpass is '':
        wr5.config(text='Password can not be empty')
    elif fpass != cpass:
        wr5.config(text='Password not matched')

    elif re.search(regex_password, fpass):
        val_cpass = cpass
        wr5.config(text='')
    else:
        wr5.config(text='Invalid password')
        flag = FALSE
    if flag is True:
        list1 = [val_name, val_email, val_user, val_cpass]
    else:
        list1 = FALSE
    return list1


def clear_field():
    text1.delete(0, 'end')
    text2.delete(0, 'end')
    text3.delete(0, 'end')
    text4.delete(0, 'end')
    text5.delete(0, 'end')
    wr1.config(text='')
    wr2.config(text='')
    wr3.config(text='')
    wr4.config(text='')
    wr5.config(text='')


window = Tk()
window.title("Sign Up Window")
window.geometry('656x384')
window.configure(background="#42A5F5")

# Title
t1 = Label(window, text='Sign Up', bg='#42A5F5', fg='white')
my_font = font.Font(size="20", family='Lato', weight='bold')
t1['font'] = my_font
t1.place(x=50, y=0)

label_font=font.Font(size='10', family='Source Sans Pro')
# Labels
l1 = Label(window, text="Full Name", bg='#42A5F5', fg='white')
l1['font'] = label_font
l1.place(x=50, y=48)
l2 = Label(window, text='Email ', bg='#42A5F5', fg='white')
l2['font'] = label_font
l2.place(x=50, y=78)
l3 = Label(window, text='Username', bg='#42A5F5', fg='white')
l3['font'] = label_font
l3.place(x=50, y=108)
l4 = Label(window, text='Password', bg='#42A5F5', fg='white')
l4['font'] = label_font
l4.place(x=50, y=138)
l5 = Label(window, text='Confirm Password', bg='#42A5F5', fg='white')
l5['font'] = label_font
l5.place(x=50, y=168)

# Warning Labels
wr1 = Label(window, text='', bg='#42A5F5', fg='red')
wr1.place(x=390, y=46)
wr2 = Label(window, text='', bg='#42A5F5', fg='red')
wr2.place(x=390, y=76)
wr3 = Label(window, text='', bg='#42A5F5', fg='red')
wr3.place(x=390, y=106)
wr4 = Label(window, text='', bg='#42A5F5', fg='red')
wr4.place(x=390, y=136)
wr5 = Label(window, text='', bg='#42A5F5', fg='red')
wr5.place(x=390, y=166)

# Entry Fields
text1 = Entry(window, width='30', border='0.5')
text1.place(x=200, y=48)
text2 = Entry(window, width='30', border='0.5')
text2.place(x=200, y=78)
text3 = Entry(window, width='30', border='0.5')
text3.place(x=200, y=108)
text4 = Entry(window,show='*', width='30', border='0.5')
text4.place(x=200, y=138)
text5 = Entry(window,show='*', width='30', border='0.5')
text5.place(x=200, y=168)

# Buttons Declaration
reset = Button(window, text='Reset', bg='#e74c3c', bd=0.6, fg='white', activebackground='#d35400', cursor='hand2',
               width='10', command=clear_field)
submit = Button(window, text='Sign up', bg='#2ecc71', bd=0.6, fg='white', cursor='hand2', activebackground='#27ae60',
                width='10', command=send_data)
reset.place(x=200, y=220)
submit.place(x=300, y=220)

window.mainloop()
