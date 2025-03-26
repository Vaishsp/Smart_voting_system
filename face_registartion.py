import tkinter as tk
#from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import cv2
##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("800x700+200+30" )
root.title("Registration Form")
root.resizable(False,False)
# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('im1.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


frame_alpr = tk.LabelFrame(root, text=" --Register-- ", width=600, height=650, bd=5, font=('times', 14, ' bold '),fg="black",bg="cornflower blue")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=50, y=50)

######################### Registration form #####################################################################

Fulllname = tk.StringVar()
adhar_card = tk.IntVar()
Voter_ID = tk.StringVar()
Password = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.StringVar()
# age = tk.IntVar()
Email = tk.StringVar()
#password1 = tk.StringVar()



# # database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user_reg"
                "(id INTEGER, Fullname TEXT, Adhar_No INTEGER, Voter_ID TEXT, password TEXT, Phone_No INTEGER)")
db.commit()


def password_check(pass1): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(pass1) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(pass1) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in pass1): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in pass1): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in pass1): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in pass1): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fulllname.get()
    addr = adhar_card.get()
    un = Voter_ID.get()
    pass1 = Password.get()
    mobile = Phoneno.get()
    Status = var.get()
    # time = age.get()
    email = Email.get()
    #cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM user_reg WHERE Voter_ID = ?')
    c.execute(find_user, [(Voter_ID.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter AdharNO")
        
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pass1 == ""):
        ms.showinfo("Message", "Please Enter valid password")
    # elif (var == False):
    #     ms.showinfo("Message", "Please Enter gender")
    elif(pass1=="")or(password_check(pass1))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    # elif (pwd != cnpwd):
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    # elif ((time > 100) or (time == 0)):
    #     ms.showinfo("Message", "Please Enter valid age")
   
    #     ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO user_reg(Fullname, Adhar_No, Voter_ID, Password, Phone_No, Email_id, status) VALUES(?,?,?,?,?,?,?)',
                (fname, addr, un, pass1, mobile, email,Status))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            root.destroy()
            





# that is for label1 registration

l2 = tk.Label(root, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=130, y=150)
t1 = tk.Entry(root, textvar=Fulllname, width=20, font=('11', 15))
t1.place(x=330, y=150)
# that is for label 2 (full name)


l3 = tk.Label(root, text="Adhar_Card No :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l3.place(x=130, y=200)
t2 = tk.Entry(root, textvar=adhar_card, width=20, font=('', 15))
t2.place(x=330, y=200)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(root, text="Voter_ID :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l5.place(x=130, y=250)
t4 = tk.Entry(root, textvar=Voter_ID, width=20, font=('', 15))
t4.place(x=330, y=250)
# that is for email address

l6 = tk.Label(root, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l6.place(x=130, y=300)
t5 = tk.Entry(root, textvar=Password, width=20, font=('', 15), show='*')
t5.place(x=330, y=300)
# phone number
l7 = tk.Label(root, text="Phone_No :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l7.place(x=130, y=350)
t6 = tk.Entry(root, textvar=Phoneno, width=20, font=('', 15))
t6.place(x=330, y=350)

l8 = tk.Label(root, text="Email:", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l8.place(x=130, y=400)
t6 = tk.Entry(root, textvar=Email, width=20, font=('', 15))
t6.place(x=330, y=400)

l7 = tk.Label(root, text="Status :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l7.place(x=130, y=450)
# gender
tk.Radiobutton(root, text="Voter", padx=5, width=5, bg="snow", font=("bold", 15), variable=var, value="Voter").place(x=330,
                                                                                                                y=450)
tk.Radiobutton(root, text="Candidate", padx=20, width=4, bg="snow", font=("bold", 15), variable=var, value="Candidate").place(
    x=450, y=450)


btn = tk.Button(root, text="Register", bg="darkred",font=("",20),fg="white", width=9, height=1, command=insert)
btn.place(x=260, y=500)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
root.mainloop()