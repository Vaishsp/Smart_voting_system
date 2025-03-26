from tkinter import *
def detect():
    import tkinter as tk
    from tkinter import ttk, LEFT, END
    from tkinter import messagebox as ms
    
    import time
    import numpy as np
    import cv2
    import os
    from PIL import Image , ImageTk     
    from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
    
    ##############################################+=============================================================
    
    root = tk.Tk()
    root.configure(background="seashell2")
    #root.geometry("1300x700")
    import sqlite3
    
    
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("smart online voting system")
    
    num=StringVar()
    otp=StringVar()
    #++++++++++++++++++++++++++++++++++++++++++++
    #####For background Image
    image2 =Image.open('img1.jpg')
    image2 =image2.resize((w,h), Image.ANTIALIAS)
    
    background_image=ImageTk.PhotoImage(image2)
    
    background_label = tk.Label(root, image=background_image)
    
    background_label.image = background_image
    
    background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
    
    
    lbl = tk.Label(root, text="Smart Online Voting System", font=('times', 30,' bold '), height=1, width=60,bg="black",fg="white")
    lbl.place(x=0, y=5)
    
    frame_alpr = tk.LabelFrame(root, text="--proceed to vote--", width=280, height=400, bd=5, font=('times', 15, ' bold '),bg="MistyRose3")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=5, y=100)
    
    import tkinter.messagebox as tsmg
    import requests
    import random
    import json

    rand=random.randint(1,999999)
    
    msg=f"Your One Time Password(OTP) is {rand}"
    
    def sms_send(a,msg):
        url="https://www.fast2sms.com/dev/bulkV2"
        params={
      
            "authorization":"VlPwmpEv6gaiZoskxqJGOX0UKHtbnfC53T8u4AdcDMjNQFYS12ijQwEVvp51O3UqYyX4sLZKaegufFWn",
            "sender_id":"SMSINI",
            "message":msg,
            "language":"english",
            "route":"p",
            "numbers":a
        }
        rs=requests.get(url,params=params)
    
    
    def send():
        a=num.get()
        if(a==""):
            tsmg.showerror("Error","Enter Your Mobile Number")
        elif (len(a)<10):
            tsmg.showerror("Error","Invalid Mobile Number")
            num.set("")
        else:
            b=tsmg.askyesno("Info",f"Your Number is {a}")
            if(b==True):
                sms_send(a,msg)
            else:
                num.set("")
    
    def check():
        c=otp.get()
        if(c==""):
            tsmg.showerror("Error","Enter OTP")
        else:
            if(str(rand)==c):
                tsmg.showinfo("Info","Successful")
                
                import face_authe
                face_authe.Test_database()
            else:
                tsmg.showerror("Error","Invalid OTP")
                num.set("")
                otp.set("")
  ###########################################################  
    # from subprocess import call
    # call(["python", "admin_login.py"])   
    
 ############################################################ 
    
   
    
    def vote():
        
    
        frame_display = tk.LabelFrame(root, text="OTP VERIFICATION ", width=600, height=400, bd=5, font=('times', 14, ' bold '),bg="MistyRose3")
        frame_display.grid(row=0, column=0, sticky='nw')
        frame_display.place(x=450, y=100)
    

        l2 = tk.Label(frame_display, text="Enter Phone No.", width=20, font=("Times new roman", 15, "bold"),bd=5, fg="black")
        l2.place(x=30, y=100)
        t1 = tk.Entry(frame_display, textvar=num,width=20, font=('', 15))
        t1.place(x=300, y=100)
        
        button2 = tk.Button(frame_display, text="Submit Mobile No.",command=send, width=20, height=1, font=('times', 15, ' bold '),bg="darkblue",fg="white")
        button2.place(x=200, y=170)
    
    
    
        l2 = tk.Label(frame_display, text="Enter OTP", width=20, font=("Times new roman", 15, "bold"),bd=5, fg="black")
        l2.place(x=30, y=240)
        t1 = tk.Entry(frame_display,textvar=otp, width=20, font=('', 15))
        t1.place(x=300, y=240)
       
        button3 = tk.Button(frame_display, text="Submit OTP",command=check, width=20, height=1, font=('times', 15, ' bold '),bg="darkblue",fg="white")
        button3.place(x=200, y=300)


    ################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
    
    
    
    
   
    
    
        
    
            
            
    def ID(): 
        frame_display = tk.LabelFrame(root, text=" ---- ", width=600, height=400, bd=5, font=('times', 14, ' bold '),bg="MistyRose3")
        frame_display.grid(row=0, column=0, sticky='nw')
        frame_display.place(x=450, y=100)
        my_conn = sqlite3.connect('upload_cad.db')
        r_set=my_conn.execute("SELECT * FROM count")
        i=1 # row value inside the loop 
        for student in r_set: 
            for j in range(len(student)):
                
                e=tk.Label(frame_display,width=50,text='Party',borderwidth=2, relief='ridge',anchor='w',bg='blue')
                e.grid(row=0,column=0)
                e=tk.Label(frame_display,width=50,text='Count',borderwidth=2, relief='ridge',anchor='w',bg='blue')
                e.grid(row=0,column=1)
                e = tk.Label(frame_display,text=student[j], width=50, fg='blue',borderwidth=2, relief='ridge', anchor="w") 
                e.grid(row=i, column=j)
                #i=1

               # e.insert(END, student[j])
            i=i+1
            
            
            
    # def t():
    #     from subprocess import call
    #     call(["python", "train.py"])             
        
    
    
    
    #################################################################################################################
    def window():
        root.destroy()
    
    
   
    button2 = tk.Button(frame_alpr, text="Cast Vote",command = vote, width=20, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
    button2.place(x=10, y=100)
    
    button3 = tk.Button(frame_alpr, text="View Result", command=ID, width=20, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
    button3.place(x=10, y=200)
    
    
    
    # button4 = tk.Button(frame_alpr, text="Display All Records", command=ID,width=20, height=1,bg="yellow4",fg="white", font=('times', 15, ' bold '))
    # button4.place(x=10, y=360)
    # ##
    # #
    # #button5 = tk.Button(frame_alpr, text="button5", command=window,width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
    # #button5.place(x=10, y=280)
    
    
    exit = tk.Button(frame_alpr, text="Exit", command=window, width=20, height=1, font=('times', 15, ' bold '),bg="darkred",fg="white")
    exit.place(x=10, y=300)
    
    
    
    root.mainloop()
detect()