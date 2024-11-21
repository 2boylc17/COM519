from tkinter import *
import sqlite3
from sqlite3 import Error

# Window
tkWindow = Tk()
tkWindow.geometry('400x250')
tkWindow.title('save and read Media file SQLite and Python ')


def send_media_to_sql():
    conn = ""
    file_path_name = 'C:\\Users\petrosyana\Downloads\Music.mp3'
    # To open a file in binary format, add 'b' to the mode parameter and "rb" mode opens the file in binary format for reading.
    with open(file_path_name, 'rb') as file:
        file_blob = file.read()
    # to see file in BLOB values
    print("[INFO] : the last 100 characters of blob = ", file_blob[:100])
    try:
        conn = sqlite3.connect('db1')
        print("[INFO] : Successful connection!")
        cur = conn.cursor()
        # to insert file_path_name and BLOB to database audio_table
        sql_insert_file_query = "INSERT INTO picture_table(file_path_name, file_blob)VALUES(?, ?)"
        cur = conn.cursor()
        cur.execute(sql_insert_file_query, (file_path_name, file_blob,))
        conn.commit()
        # message to test
        print("[INFO] : The blob for ", file_path_name, " sent and saved in the database audio_table.")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        # else:
        # error = "Oh shucks, something is wrong here."
