import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("GUI")
#------------------Frame----------------------
image2 =Image.open('im3.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "Voter.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "admin_login.py"])   
    


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image



lbl = tk.Label(root, text="Smart Online Voting System", font=('times', 40,' bold '), height=1, width=41,bg="black",fg="white")
lbl.place(x=0, y=5)

framed = tk.LabelFrame(root, text="--SMART ONLINE VOTING SYSTEM--", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=400, y=200)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(framed, text='Admin',width=15,height=3,bg='dark blue',fg='white',command=login,font='bold').place(x=250,y=80)
button1 = tk.Button(framed, text='User',width=15,height=3,bg='dark blue',fg='white',command=reg,font='bold').place(x=80,y=80)


root.mainloop()
