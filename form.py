import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk
from tkinter.filedialog import asksaveasfile 
from tkinter import font as tkFont
from tkinter import messagebox

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import ImageGrab




root = Tk()
root.title('FACE RECOGNITION')
root.geometry('800x450')



frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )





def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def save(): 
    files = [('Jpg Files', '*.jpg'),  
             ('Png Files', '*.png'), 
             ('JPEG Files', '*.jpeg'),
             ('All Files', '*.*')] 
    file = asksaveasfile(filetypes = files, defaultextension = files)
    

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def facereg():


    import time
      
    progress['value']=20
    root.update_idletasks()
    time.sleep(7)
    progress['value']=50
    root.update_idletasks()
    time.sleep(1)
  

    video_capture = cv2.VideoCapture(0)
 
    path = 'faceimages'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)
    


    encodeListKnown = findEncodings(images)
    print('Encoding Complete')  


    progress['value']=80
    root.update_idletasks()

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    time.sleep(1)
    progress['value']=100
    
    messagebox.showinfo("IMPORTANT","PRESS 'Q' TO CLOSE FACIAL RECOGNITION")

    while True:

      
        img = ImageGrab.grab()
        img_np = np.array(img)

        frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
       
        

        
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

       
        rgb_small_frame = small_frame[:, :, ::-1]

        
        if process_this_frame:
            
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
               
                matches = face_recognition.compare_faces(encodeListKnown, face_encoding)
                name = "Unknown"

               
                face_distances = face_recognition.face_distance(encodeListKnown, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = classNames[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame


        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

           
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

       
        cv2.imshow('Video', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    
    video_capture.release()
    cv2.destroyAllWindows()







s=Style()
s.configure("TProgressbar",foreground="red",background="red",thickness=40)

label1=Label(bottomframe,font="arial 15 bold")
label1.pack(side = BOTTOM)

progress=Progressbar(bottomframe,orient = HORIZONTAL,length=400,mode='determinate')
progress.pack(side = BOTTOM)





canvas = Canvas(width=350, height=200, bg='blue')
canvas.pack(expand=YES, fill=BOTH)
image = ImageTk.PhotoImage(file="faceback1.jpg")
canvas.create_image(0, 0, image=image, anchor=NW)







menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)


root.config(menu=menubar)



hel = tkFont.Font(family='CORNERSTONE', size=10, weight=tkFont.BOLD)
comi= tkFont.Font(family='Comic Sans MS', size=10, weight=tkFont.BOLD)


 
x1=Button(root,text="UPLOAD",command = lambda : save(),font=hel)
x1.config(width="13",height="2",bg="#E74C3C ",activebackground="#EC7063")
x1.place(relx = 0.1, rely = 0.3)



x2=Button(root,text="SCAN",font=hel,command=facereg)
x2.config(width="13",height="2",bg="#2ECC71",activebackground="#1D8348")
x2.place(relx = 0.1, rely = 0.5)


btn1=Button(root,font=hel,text="EXIT",width="13",height="2",bg="#F4D03F",activebackground="#F9E79F",command=root.quit)
btn1.place(relx = 0.1, rely = 0.7) 


""" b1=Button(root,font=hel,text="CLICK",width="13",height="2",bg="#F4D03F",activebackground="#F9E79F",command=start)
b1.place(relx = 0.1, rely = 0.9) """




root.mainloop()