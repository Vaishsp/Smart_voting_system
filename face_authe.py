
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
    
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
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
                    
                    
                   #  with sqlite3.connect('evaluation.db') as db:
                   #  c = db.cursor()
            
                   #  # Find user If there is any take proper action
                   #  db = sqlite3.connect('evaluation.db')
                   #  cursor = db.cursor()
                   #  cursor.execute("CREATE TABLE IF NOT EXISTS user_reg"
                   #                     "(Fullname TEXT, Adhar_No INTEGER, Voter_ID TEXT, Password TEXT, Phoneno INTEGER,Email_id TEXT,status TEXT)")
                   #  db.commit()
                   # # find_entry = ('SELECT id FROM user_reg WHERE username = ? ')
                   #  #c.execute(find_entry, [(username.get()), (password.get())])
                   #  #result = c.fetchall()
                   #  find_entry1 = ('SELECT id FROM user_reg WHERE id = ?')
                   #  c.execute(find_entry1, [(id.get())])
                   #  result1 = c.fetchall()
                   #  print(result1)
                    print(id)
                    with open(r"id.txt", 'w') as f:
                      f.write(str(id))
                    
                    from subprocess import call
                    call(["python", "cast_vote.py"]) 
    
                    #i=0 # row value inside the loop 
                    # for student in r_set: 
                        
                        # for j in range(len(student)):
                        #     e =tk.Entry(frame_display, width=10, fg='blue') 
                        #     e.grid(row=i, column=j) 
                        #     e.insert(END, student[j])
                # reg=registerno.get()
                # print(reg)
              
                 
                    
                    cam.release()
                    cv2.destroyAllWindows()
                else:
    #                print(confidence)
                     id = "unknown Person Identified"
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
                # from subprocess import call
                # call(["python", "smartmirror.py"])
    
         
            # k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    #        if k == 27:
    #            break
            if cv2.waitKey(1) == ord('Q'):
                break
    
        # Do a bit of cleanup
    #    print("\n [INFO] Exiting Program and cleanup stuff")
    #    cam.release()
    #    cv2.destroyAllWindows()