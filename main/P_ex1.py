from tkinter import *
from tkinter import messagebox
from functools import partial
import sqlite3
import hashlib
import xml.etree.ElementTree as ET

# Window
tkWindow = Tk()  
tkWindow.geometry('400x250')  
tkWindow.title('Tkinter SQLite Login Form example ')

def read_XML(user_input, pass_input):
        # Passing the path of the
        # xml document to enable the
        # parsing process
        tree = ET.parse('login_details.xml')
        # getting the parent tag of
        # the xml document
        root = tree.getroot()

        # printing the root (parent) tag
        # of the xml document, along with
        # its memory location
        print(root)
        # printing the attributes of the
        # first tag from the parent
        print(root[0].attrib)

        # printing the text contained within

        # the parent
        for row in root[0]:
                #print('row', row,'root', root[0],'text', row.text, 'attrib', root[0].text)
                if row.text == user_input:
                        print('Username hash =', row.text)
                elif row.text == pass_input:
                        print('Password hash =', row.text)

def write_xml():
        connection_obj = sqlite3.connect("newdb.db")
        cursor_obj = connection_obj.cursor()
        cursor_obj.execute("SELECT * FROM login_details;")
        get_login_details=cursor_obj.fetchall()
        # This is the parent (root) tag
        # onto which other tags would be
        # created
        data = ET.Element('user')
        # Adding a subtag named `login`
        # inside our root tag
        element1 = ET.SubElement(data, 'login_dartais')
        # Adding subtags under the `login`
        # subtag
        for row in get_login_details:
                s_elem1 = ET.SubElement(element1, 'login')
                s_elem2 = ET.SubElement(element1, 'password')
                # Adding attributes to the tags under
                # `items`
                #s_elem1.set('type', 'login')
                #s_elem2.set('type', 'Declined')
                # Adding text between the `E4` and `D5`
                # subtag
                s_elem1.text = row[0]
                s_elem2.text = row[1]
        # Converting the xml data to byte object,
        # for allowing flushing data to file
        # stream
        b_xml = ET.tostring(data)
        # Opening a file under the name `items2.xml`,
        # with operation mode `wb` (write + binary)
        with open("login_details.xml", "wb") as f:
            f.write(b_xml)


def recover_xml():
        connection_obj = sqlite3.connect("newdb.db")
        cursor_obj = connection_obj.cursor()
        tree = ET.parse('login_details.xml')
        root = tree.getroot()
        user_input = None
        inc = 0
        for num in root[0]:
                if inc % 2 == 0:
                        user_input = num.text
                        print("user", user_input)
                        inc += 1
                else:
                        pass_input = num.text
                        print("pass", pass_input)
                        cursor_obj.execute("INSERT INTO login_details VALUES('"+user_input+"', '"+pass_input+"')")
                        inc = 0

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
                print("success")
                messagebox.showinfo("showinfo", "correct login and password")
        else:
                print("fail")
                messagebox.showwarning("Warning", "Incorrect login or password")

        for row in output1:
                print('row', row)

        connection_obj.commit()

        # Close the connection
        connection_obj.close()
        read_XML(dec_username, dec_password)
       

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
        write_xml()

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
loginButton1 = Button(tkWindow, text="Login", command=recover_xml).grid(row=3, column=0)

register_customer = partial(register_customer, username, password)
#register
loginButton2 = Button(tkWindow, text="Register", command=register_customer).grid(row=3, column=1)

 


tkWindow.mainloop()
