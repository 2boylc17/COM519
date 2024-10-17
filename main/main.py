from tkinter import *
from tkinter import messagebox
from functools import partial
import sqlite3
import hashlib

# Window
tkWindow = Tk()
tkWindow.geometry('400x250')
tkWindow.title('Tkinter SQLite Login Form example ')

def newCustomer():
    print('New Customer')
    lastNameLabel = Label(tkWindow, text='Last Name').grid(row=0, column=0)
    lastName = StringVar()
    lastNameEntry = Entry(tkWindow, textvariable=lastName).grid(row=0, column=1)
    firstNameLabel = Label(tkWindow, text='First Name').grid(row=1, column=0)
    firstName = StringVar()
    firstNameEntry = Entry(tkWindow, textvariable=lastName).grid(row=1, column=1)
    addressLabel = Label(tkWindow, text='Address').grid(row=2, column=0)
    address = StringVar()
    addressEntry = Entry(tkWindow, textvariable=lastName).grid(row=2, column=1)
    cityLabel = Label(tkWindow, text='City').grid(row=3, column=0)
    city = StringVar()
    cityEntry = Entry(tkWindow, textvariable=lastName).grid(row=3, column=1)
    #loginButton1.grid(row=4,column =0)
    x=6



def updateStock():
    print('Update Stock')

x=4
y=0
loginButton1 = Button(tkWindow, text="New Customer", command=newCustomer).grid(row=x, column=y)
loginButton2 = Button(tkWindow, text="Update Stock", command=updateStock).grid(row=4, column=1)

tkWindow.mainloop()
