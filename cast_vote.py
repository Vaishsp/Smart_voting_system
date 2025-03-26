
import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  
from tkinter import messagebox as ms

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="lightblue")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Cast vote")
#------------------Frame----------------------

#Fulllname = tk.StringVar()
vote = tk.IntVar()
id = tk.IntVar()

# def login():
    
# ##### tkinter window ######
    
#     print("log")
#     from subprocess import call
#     call(["python", "Login1.py"])   
    


# #++++++++++++++++++++++++++++++++++++++++++++
# #####For background Image
image2 =Image.open('im3.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


# Python program to convert a list to string
    
# Function to convert  
import functools
import operator
 
 
def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str
 
 
def cast_vote():
    
    #fname = Fulllname.get()
    vote1 = vote.get()
    
    f1 = open("id.txt","r")
    id = f1.read()
    print(id)
    f1.close()
    
    with sqlite3.connect('upload_cad.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM cast_vote WHERE id = ?')
    c.execute(find_user, [(id)])

   
    if (c.fetchall()):
        ms.showerror('Error!', 'You Already Voted')
  
    
    else:
        conn = sqlite3.connect('upload_cad.db')
        with conn:
             cursor = conn.cursor()
             cursor.execute('INSERT INTO cast_vote(id, vote) VALUES(?,?)',
                    (id, vote1))
             if vote1 == 1:
                find_user = ('SELECT Count FROM count WHERE Party = 1')
                print(find_user)
                c.execute(find_user)
                s = c.fetchall()
                print(s)
                print(type(s))
                a = s[0]
                print(a)
                #print(listToString(s))
                str1 = convertTuple(a)
                print(str1)
                 
                str2 = str1+1
                print(str2)
               # str2 = print(int(str2))
               # conn = sqlite3.connect('upload_cad.db')
                with conn:
                     cursor = conn.cursor()
                     cursor.execute("""UPDATE  count SET Count= '{0}' WHERE Party = 1 """.format(str2))
                     
                     conn.commit()
                     cursor.close()
                     db.close()
                
                # elif vote1 == 2:
                # find_user = ('SELECT Count FROM count WHERE Party = 1')
                # print(find_user)
                # c.execute(find_user)
                # s = c.fetchall()
                # print(s)
                # print(type(s))
                # a = s[0]
                # print(a)
                # #print(listToString(s))
                # str1 = convertTuple(a)
                # print(str1)
                 
                # str2 = str1+1
                # print(str2)
                # str2 = print(int(str2))
                # conn = sqlite3.connect('upload_cad.db')
                # with conn:
                #      cursor = conn.cursor()
                #      cursor.execute('INSERT INTO count (Count) VALUES(?)',(str2))
                #      conn.commit()
                #      conn.close()
                     
                # elif vote1 == 3:
                # find_user = ('SELECT Count FROM count WHERE Party = 1')
                # print(find_user)
                # c.execute(find_user)
                # s = c.fetchall()
                # print(s)
                # print(type(s))
                # a = s[0]
                # print(a)
                # #print(listToString(s))
                # str1 = convertTuple(a)
                # print(str1)
                 
                # str2 = str1+1
                # print(str2)
                # str2 = print(int(str2))
                # conn = sqlite3.connect('upload_cad.db')
                # with conn:
                #      cursor = conn.cursor()
                #      cursor.execute('INSERT INTO count (Count) VALUES(?)',(str2))
                #      conn.commit()
                #      conn.close()
               
                
                
                
                #count = count+1
             # elif vote1 == 2:
             #     vote1 ++
    
             conn.commit()
             db.close()
             ms.showinfo('Success!', 'Vote submited Successfully !')
                # window.destroy()
            

lbl = tk.Label(root, text="Cast Vote", font=('times', 35,' bold '), height=1, width=43,bg="darkred",fg="white")
lbl.place(x=35, y=15)

# framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="pink")
# framed.grid(row=0, column=0, sticky='nw')
# framed.place(x=20, y=100)
#++++++++++++++++++++++++++++++++++++++++++++

# l7 = tk.Label(root, text="AAP :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)

# l7 = tk.Label(root, text="BJP :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)

# l7 = tk.Label(root, text="CONG :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)

# l7 = tk.Label(root, text="NOTA :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)

# l7 = tk.Label(root, text="SS :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)
# # gender
image1 = Image.open(r'C:/CPP project/Smart_Voting_System/img/aap.png')
image1 = image1.resize((100, 100), Image.ANTIALIAS)

image_lab1 = ImageTk.PhotoImage(image1)

img_lb = tk.Label(root, image=image_lab1)

img_lb.image = image_lab1

img_lb.place(x=450, y=120)  # , relwidth=1, relheight=1)

tk.Radiobutton(root, text="AAP", padx=5, width=5, bg="snow", font=("bold", 15),variable=vote,value=1).place(x=650,y=150)


image2 = Image.open(r'C:/CPP project/Smart_Voting_System/img/bjp.png')
image2 = image2.resize((100, 100), Image.ANTIALIAS)

image_lab2 = ImageTk.PhotoImage(image2)

img_lb1 = tk.Label(root, image=image_lab2)

img_lb1.image = image_lab2

img_lb1.place(x=450, y=250)  

tk.Radiobutton(root, text="BJP", padx=5, width=4, bg="snow", font=("bold", 15),variable=vote,value=2).place(x=650, y=280)

image3 = Image.open(r'C:/CPP project/Smart_Voting_System/img/cong.jpg')
image3 = image3.resize((100, 100), Image.ANTIALIAS)

image_lab3 = ImageTk.PhotoImage(image3)

img_lb2 = tk.Label(root, image=image_lab3)

img_lb2.image = image_lab2

img_lb2.place(x=450, y=380) 

tk.Radiobutton(root, text="CONG", padx=5, width=5, bg="snow", font=("bold", 15),variable=vote,value=3).place(x=650,y=410)

# image2 = Image.open(r'E:/Smart_Voting_System/img/aap.png')
# image2 = image2.resize((100, 100), Image.ANTIALIAS)

# image_lab2 = ImageTk.PhotoImage(image2)

# img_lb1 = tk.Label(root, image=image_lab2)

# img_lb1.image = image_lab2

# img_lb1.place(x=450, y=250) 


# tk.Radiobutton(root, text="NOTA", padx=5, width=4, bg="snow", font=("bold", 15), value=4).place(x=650, y=450)

# image2 = Image.open(r'E:/Smart_Voting_System/img/aap.png')
# image2 = image2.resize((100, 100), Image.ANTIALIAS)

# image_lab2 = ImageTk.PhotoImage(image2)

# img_lb1 = tk.Label(root, image=image_lab2)

# img_lb1.image = image_lab2

# img_lb1.place(x=450, y=250) 

# tk.Radiobutton(root, text="SS", padx=5, width=5, bg="snow", font=("bold", 15), value=5).place(x=650,y=550)
# # tk.Radiobutton(root, text="BJP", padx=20, width=4, bg="snow", font=("bold", 15), value=2).place(
# #     x=440, y=350)



# image2 = Image.open(r'E:/Smart_Voting_System/img/aap.png')
# image2 = image2.resize((100, 100), Image.ANTIALIAS)

# image_lab2 = ImageTk.PhotoImage(image2)

# img_lb1 = tk.Label(root, image=image_lab2)

# img_lb1.image = image_lab2

# img_lb1.place(x=450, y=250) 






btn = tk.Button(root, text="Submit", bg="darkred",font=("",20),fg="white", command = cast_vote,width=9, height=1)
btn.place(x=500, y=550)



#####For background Image
# button1 = tk.Button(framed, text='Login Now',width=15,height=3,bg='dark blue',fg='white',command=login,font='bold').place(x=20,y=35)
# button1 = tk.Button(framed, text='Register',width=17,height=3,bg='dark blue',fg='white',command=reg,font='bold').place(x=250,y=35)


root.mainloop()
