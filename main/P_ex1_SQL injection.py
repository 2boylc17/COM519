from tkinter import *
from tkinter import messagebox
from functools import partial
import sqlite3




# Window
tkWindow = Tk()  
tkWindow.geometry('400x250')  
tkWindow.title('Tkinter SQLite Login Form example ')




def validateLogin(username, password):
	
        connection_obj = sqlite3.connect("db1")
        cursor_obj = connection_obj.cursor()

        value_username=username.get()
        value_password=str(password.get())


        
        
        cursor_obj.execute("SELECT * FROM login_details WHERE User_Login='"+value_username+"'"+" AND User_password='"+
                           str(value_password)+"'")
        output1=cursor_obj.fetchall()

        if len(output1)>0:
                print("hi")
                messagebox.showinfo("showinfo", "correct login and password")
        else:
                print("no")
                messagebox.showwarning("Warning","Incorrect login or password")
                
        for row in output1:
                print(row)
  
        connection_obj.commit() 
  
        # Close the connection 
        connection_obj.close()
       

def register_customer(username, password):
	#user01', 1111); DELETE FROM login_details; -- #input this as a username to inject SQL to delete all data
        #user01', 1111); update login_details set user_password ='000000' where user_login='user01'; -- # to update all user_passwords to 00000 

        connection_obj = sqlite3.connect("db1")
        cursor_obj = connection_obj.cursor()
        value_username=str(username.get())
        value_password=str(password.get())
           
        if len(value_password)>=5 and len(value_username)>=5:
                #cursor_obj.execute("INSERT INTO login_details VALUES ? ?", username,password)

                #cursor_obj.executescript(f"INSERT INTO login_details VALUES ('{value_username}', {value_password})")

                #cursor_obj.execute("INSERT INTO login_details VALUES (?, ?)", (value_username, value_password))
                
                cursor_obj.executescript("insert into login_details values('"+value_username+"', '"+value_password+"')")
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

validateLogin = partial(validateLogin, username, password)

# Login button
loginButton1 = Button(tkWindow, text="Login", command=validateLogin).grid(row=3, column=0)

register_customer = partial(register_customer, username, password)
#register
loginButton2 = Button(tkWindow, text="Register", command=register_customer).grid(row=3, column=1)

 


tkWindow.mainloop()
