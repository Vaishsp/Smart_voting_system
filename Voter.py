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
    root.title("Smart Online Voting System")
    
    
    #++++++++++++++++++++++++++++++++++++++++++++
    
    lbl = tk.Label(root, text="Smart Online Voting System", font=('times', 30,' bold '), height=1, width=60,bg="black",fg="white")
    lbl.place(x=0, y=5)
    
    frame_alpr = tk.LabelFrame(root, text="--REGISTER/LOGIN--", width=280, height=600, bd=5, font=('times', 15, ' bold '),bg="lightblue")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=5, y=100)
    
    frame_display = tk.LabelFrame(root, text=" --LIST OF VOTERS-- ", width=700, height=550, bd=5, font=('times', 14, ' bold '),bg="lightblue")
    frame_display.grid(row=0, column=0, sticky='nw')
    frame_display.place(x=330, y=100)
    ################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
    
    
    def Create_database():
            
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        cap = cv2.VideoCapture(0)
        
    #    id = input('enter user id')
        id=entry2.get()
        
        sampleN=0;
        
        while 1:
        
            ret, img = cap.read()
        
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
            for (x,y,w,h) in faces:
        
                sampleN=sampleN+1;
        
                cv2.imwrite("facesData/User."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
        
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
                cv2.waitKey(100)
        
            cv2.imshow('img',img)
        
            cv2.waitKey(1)
        
            if sampleN > 40:
        
                break
        
        cap.release()
        entry2.delete(0,'end')
        cv2.destroyAllWindows()
    
    def update_label(str_T):
        #clear_img()
        result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='blue1', fg='black')
        result_label.place(x=350, y=500)
    
    def Train_database():
               
        recognizer =cv2.face.LBPHFaceRecognizer_create();
        
        path="facesData"
        
        def getImagesWithID(path):
        
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]   
        
         # print image_path   
        
         #getImagesWithID(path)
        
            faces = []
        
            IDs = []
        
            for imagePath in imagePaths:      
        
          # Read the image and convert to grayscale
        
                facesImg = Image.open(imagePath).convert('L')
        
                faceNP = np.array(facesImg, 'uint8')
        
                # Get the label of the image
        
                ID= int(os.path.split(imagePath)[-1].split(".")[1])
        
                 # Detect the face in the image
        
                faces.append(faceNP)
        
                IDs.append(ID)
        
                cv2.imshow("Adding faces for traning",faceNP)
        
                cv2.waitKey(10)
        
            return np.array(IDs), faces
        
        Ids,faces  = getImagesWithID(path)
        
        recognizer.train(faces,Ids)
        
        recognizer.save("trainingdata.yml")
        
        cv2.destroyAllWindows()
    
        
    
    
    
    def writeTofile(data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)
            #return abc
        
        print("Stored blob data into: ", filename, "\n")
        return filename
        
    def Test_database():
        flag=0
        recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 100)
    #    recognizer = cv2.face.FisherFaceRecognizer(0, 3000);
        
        recognizer.read('trainingdata.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath);
        font = cv2.FONT_HERSHEY_SIMPLEX
        #iniciate id counter
        id = 0
        # names related to ids: example ==> Marcelo: id=1,  etc
        #names = ['None', 'Criminal person identified', 'Missing person', 'Criminal person identified', 'Criminal person identified', 'Missing person','Missing person'] 
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height
        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)
        
        while True:
            ret, img =cam.read()
    #        img = cv2.flip(img, -1) # Flip vertically
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray,1.3,8,minSize = (int(minW), int(minH)))
    #        faces = faceCascade.detectMultiScale( 
    #            gray,
    #            scaleFactor = 1.2,
    #            minNeighbors = 5,
    #            minSize = (int(minW), int(minH)),
    #           )
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                
                # If confidence is less them 100 ==> "0" : perfect match
                
                if (confidence < 60):
                    #print(id)
                    #name = names[id]
                    id = id
                    print(type(id))
                    #name = names[id]
                    #id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                    
                             
                    #cv2.putText(img,str(name),(x+5,y-5),font,1,(255,255,255),2)
                    cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
                    # my_conn = sqlite3.connect('evaluation.db')
                    # r_set=my_conn.execute("select * from registration where id =" + str(id) +"");
                    cv2.putText(img,"Person Identified"+str(id),(x+5,y-5),font,1,(255,255,255),2)
                     
                    ms.showinfo("Person Identified","Person Identified Successfully !!")
                      
    
                  
                    
                    cam.release()
                    cv2.destroyAllWindows()
                    from subprocess import call
                    call(["python", "GUI_R_V.py"])
                else:
    #                print(confidence)
                     id = "Person Identified"
                     confidence = "  {0}%".format(round(100 - confidence))
                    
                     cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                     cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)  
                
            
    
    #        time.sleep(0.2)
            cv2.imshow('camera',img) 
    #        print(flag)
            if flag==10:
                flag=0
                cam.release()
                cv2.destroyAllWindows()
                
    
         
            # k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    #        if k == 27:
    #            break
            if cv2.waitKey(1) == ord('Q'):
                break
    
        # Do a bit of cleanup
    #    print("\n [INFO] Exiting Program and cleanup stuff")
    #    cam.release()
    #    cv2.destroyAllWindows()
    #    

    
    
    

    
    def reg():
        
    ##### tkinter window ######
        
        from subprocess import call
        call(["python", "face_registartion.py"]) 
    
    
        
    
            
            
    def ID():     
        my_conn = sqlite3.connect('evaluation.db')
        r_set=my_conn.execute("SELECT * FROM user_reg")
        i=0 # row value inside the loop 
        for student in r_set: 
            for j in range(len(student)):
                e =tk.Entry(frame_display, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, student[j])
            i=i+1
            
            
            
    # def t():
    #     from subprocess import call
    #     call(["python", "train.py"])             
        
    
    
    
    #################################################################################################################
    def window():
        root.destroy()
    
    
    button1 = tk.Button(frame_alpr, text="Voter Registration", command=reg,width=15, height=1, font=('times', 15, ' bold '),bg="darkblue",fg="white")
    button1.place(x=10, y=100)
    
    button1 = tk.Button(frame_alpr, text="Create Face Data", command=Create_database,width=15, height=1, font=('times', 15, ' bold '),bg="darkblue",fg="white")
    button1.place(x=10, y=160)
    
    entry2=tk.Entry(frame_alpr,bd=2,width=7)
    entry2.place(x=210, y=160)
    
    button2 = tk.Button(frame_alpr, text="Train Face Data", command=Train_database, width=20, height=1, font=('times', 15, ' bold '),bg="darkblue",fg="white")
    button2.place(x=10, y=220)
    
    #frame_login = tk.LabelFrame(frame_alpr, text=" If you have already registered ,\n please LOGIN to vote! ", width=250, height=30, bd=5, font=('times', 8, ' bold '),bg="grey")
   # frame_login.grid(row=0, column=0, sticky='nw')
    #frame_login.place(x=20, y=260)
    
    button3 = tk.Button(frame_alpr, text="LOGIN", command=Test_database, width=20, height=1, font=('times', 15, ' bold '),bg="darkblue",fg="white")
    button3.place(x=10, y=270)
    
    
    
    button4 = tk.Button(frame_alpr, text="Display All Records", command=ID,width=20, height=1,bg="darkblue",fg="white", font=('times', 15, ' bold '))
    button4.place(x=10, y=330)
    ##
    #
    #button5 = tk.Button(frame_alpr, text="button5", command=window,width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
    #button5.place(x=10, y=280)
    
    
    exit = tk.Button(frame_alpr, text="Exit", command=window, width=20, height=1, font=('times', 15, ' bold '),bg="darkred",fg="white")
    exit.place(x=10, y=410)
    
    
    
    root.mainloop()
detect()