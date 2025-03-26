import sqlite3
import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
from tkinter.filedialog import askopenfilename
import os
import cv2
global id 

window = tk.Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
window.title(" FORM")
window.configure(background="grey")
global file
Fullname = tk.StringVar()
sym = tk.StringVar()

file1=tk.StringVar()
sym_name = tk.StringVar()

value = random.randint(1, 1000)
print(value)

image2 = Image.open('im1.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

frame_alpr = tk.LabelFrame(window, text=" ----- ", width=600, height=450, bd=5, font=('times', 15, ' bold '),bg="pink")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=400, y=150)



def show():
    global file
    file = askopenfilename(initialdir=r'C:/CPP project/Smart_Voting_System/img', title='Select Image',
                                       filetypes=[("all files", "*.*")])
    
    image3 =Image.open(file)
    image3 =image3.resize((450,280), Image.ANTIALIAS)
    print(file)
    return file
    


def convertToBinaryData(filename):             #We have to add image to database thats why use this function to convert image into binary format
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB():
    global file
    fname = Fullname.get()
   
    #un = username.get()
    
    sym = file
    Photo = convertToBinaryData(sym)
    print(sym)
    sym_n = sym_name.get()
    
    try:
        sqliteConnection = sqlite3.connect('upload_cad.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO cand
                                  (Name, symbol,  sym_name) 
                                  VALUES (?,?,?)"""

        empPhoto = convertToBinaryData(sym)
        #resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (fname,empPhoto,sym_n)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
        

        

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
    window.destroy()




l1 = tk.Label(window, text="Candidate Form", font=("Times new roman", 30, "bold"), bg="Black", fg="white")
l1.place(x=500, y=5)

# that is for label1 registration

l2 = tk.Label(frame_alpr, text="Candidate Name :", width=15, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=50, y=50)
t1 = tk.Entry(frame_alpr, textvar=Fullname, width=30, font=('', 15))
t1.place(x=250, y=50)
# that is for label 2 (full name)



l4 = tk.Button(frame_alpr, text="Upload Photo :", width=15, font=("Times new roman", 15, "bold"), bg="snow",command=show)
l4.place(x=50, y=150)
#file1=show(file)
#t3 = tk.Entry(window, textvar=file1, width=20, font=('', 15))
#t3.place(x=330, y=450)

l10 = tk.Label(frame_alpr, text="Party Name", width=15, font=("Times new roman", 15, "bold"), bg="snow")
l10.place(x=50, y=250)

t10 = tk.Entry(frame_alpr, textvar=sym_name, width=30, font=('', 15))
t10.place(x=250, y=250)

btn = tk.Button(frame_alpr, text="Submit", bg="darkred",font=("",20),fg="white", width=9, height=1, command=insertBLOB)
btn.place(x=220, y=320)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()