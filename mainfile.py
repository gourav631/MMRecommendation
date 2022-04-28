from ast import Index
from enum import auto
from tokenize import Name
from deepface import DeepFace
from numpy import size
import pandas as pd
from cv2 import *
import cv2
import time
import threading
import tkinter
from tkinter import *
from tkhtmlview import HTMLLabel
from PIL import Image, ImageTk
from tkinter import messagebox



#----------------------GLOBAL VARIABLES------------------------------
cam_port = 0
cam = cv2.VideoCapture(cam_port)
root = Tk()
# Set Geometry
root.geometry("750x800")
mainlabel = HTMLLabel(root, html="""
    <div style="color:black;">
   <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/7gNfiBDwnqG3jHnlV3fsO3?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></i
   frame>
</div>
    """)

mainlabel.grid(row=0,column=1)
#----------------------CAMERA OPEN ALWAYS----------------------------

opencvlabel = Label(root,width=720,height=300)

def opencvfunc():
  cv2image= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
  img = Image.fromarray(cv2image)
  # Convert image to PhotoImage
  imgtk = ImageTk.PhotoImage(image = img)
  opencvlabel.imgtk = imgtk
  opencvlabel.configure(image=imgtk)
  opencvlabel.after(1, opencvfunc)
  
opencvlabel.grid(row=0,column=0)
#---------------------TAKE SNAPSHOT AND DETECT----------------------

def restall():
  result, image = cam.read()
  cv2.imwrite('abcd.png',image)
  obj = DeepFace.analyze(img_path = "abcd.png", actions = ['emotion'],enforce_detection=False)
  s = obj.get('dominant_emotion')
  print(s)
  s2 = "C:\\Users\\gurne\\OneDrive\\Desktop\\MAIN_FOLDER\\premade\\allemotions.csv"
  print(s2)
  df = pd.read_csv(s2)
  df = df[df.Emotion==s]
  df2 = df.sample(n=5)
  df3 = df2['Name']
  print(df3)
  messagebox.showinfo( "RESULT", "IMAGE CAPTURED")
  t = Text(root,height=8, width=60, font=("Courier", 14))
  label = Label(root, text= "Recommended Songs for "+s+" mood")
  label.configure(font=("Courier", 20))
  label.place(x=118,y=500)
  for x in df2['Name']:
    t.insert(END, x + '\n')
  t.place(x=48,y=550)
  t.config(state='disabled')

t1 = threading.Thread(target=opencvfunc).start()

sublabel = Label(root,width=720)
sub = tkinter.Button(sublabel,text="CLICK TO CAPTURE",command=lambda:threading.Thread(target=restall).start(),height=3,width=15,border=2).pack()
sublabel.grid(row=1,column=0)




tkinter.mainloop() 