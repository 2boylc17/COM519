from tkinter import *
from tkinter import messagebox
from functools import partial
import sqlite3
import hashlib

# Window
tkWindow = Tk()  
tkWindow.geometry('400x250')  
tkWindow.title('Tkinter SQLite Login Form example ')

def validate_login(user_name, pass_word):
        connection_obj = sqlite3.connect("newdb.db")
        cursor_obj = connection_obj.cursor()

        value_username = user_name.get()
        value_password = str(pass_word.get())
        dec_username = hashlib.sha256(value_username.encode()).hexdigest()
        dec_password = hashlib.sha256(value_password.encode()).hexdigest()
        cursor_obj.execute(
                "SELECT * FROM login_details WHERE User_Login='" + dec_username + "'" + " AND User_password='" + dec_password + "'")
        output1 = cursor_obj.fetchall()

        if len(output1) > 0:
                print("hi")
                messagebox.showinfo("showinfo", "correct login and password")
        else:
                print("no")
                messagebox.showwarning("Warning", "Incorrect login or password")

        for row in output1:
                print(row)

        connection_obj.commit()

        # Close the connection
        connection_obj.close()
       

def register_customer(user_name, pass_word):
	
        connection_obj = sqlite3.connect("newdb.db")
        cursor_obj = connection_obj.cursor()
        value_username=user_name.get()
        value_password=str(pass_word.get())
        #encrypton
        #encode(value_password, password = 'mypass')
        enc_username = hashlib.sha256(value_username.encode()).hexdigest()
        enc_password = hashlib.sha256(value_password.encode()).hexdigest()
        
        value_password.encode()
        
        if len(value_password)>5 and len(value_username)>5:
                #cursor_obj.execute("insert into login_details values('"+value_username+"', '"+str(encvalue_password)+"')")
                cursor_obj.execute("insert into login_details values('"+enc_username+"', '"+enc_password+"')")
                messagebox.showinfo("showinfo", "user registred")
        else:
                messagebox.showwarning("Warning","Incorrect length of password and login - min 5 symbols")
                
        connection_obj.commit() 
  
        # Close the connection 
        connection_obj.close()
       

# Username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

# Password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validate_login, username, password)

# Login button
loginButton1 = Button(tkWindow, text="Login", command=validateLogin).grid(row=3, column=0)

register_customer = partial(register_customer, username, password)
#register
loginButton2 = Button(tkWindow, text="Register", command=register_customer).grid(row=3, column=1)

 


tkWindow.mainloop()
