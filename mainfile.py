from sqlite3 import Row
from deepface import DeepFace
import pandas as pd
from cv2 import *
import cv2
import time
import threading
import tkinter
from tkinter import *
from tkhtmlview import HTMLLabel

#----------------------GLOBAL VARIABLES------------------------------
cam_port = 0
cam = cv2.VideoCapture(cam_port)
root = Tk()
 
# Set Geometry
root.geometry("400x400")
my_label = HTMLLabel(root, html="""
        <h1>Music Mood recommender</h1>
    <div class="row">
      <div class="column1">
        <div id="camera"></div>
        <input
          type="button"
          id="Take Snapshot"
          value="Take Snapshot"
          onClick="take_snapshot()"
        />
        <div id="results"></div>
      </div>
      <div class="column2">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Music</th>
              <th scope="col">which</th>
              <th scope="col">goes</th>
              <th scope="col">your Mood</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td>Mark</td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td>Jacob</td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td>Larry</td>
            </tr>
            <tr>
              <th scope="row">4</th>
              <td>Larry</td>
            </tr>
            <tr>
              <th scope="row">5</th>
              <td>Larry</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """)

my_label.grid(row=0,column=0)
#----------------------CAMERA OPEN ALWAYS----------------------------
def opencvfunc():
  while(True):
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
      cv2.destroyAllWindows()
      break
    
#---------------------TAKE SNAPSHOT AND DETECT----------------------
def restall():
  time.sleep(5)
  result, image = cam.read()
  cv2.imshow('img1',image)
  cv2.imwrite('abcd.jpg',image)
  obj = DeepFace.analyze(img_path = "abcd.jpg", actions = ['emotion'])
  s = obj.get('dominant_emotion')
  print(s)
  s2 = "C:\\Users\\gurne\\OneDrive\\Desktop\\MAIN_FOLDER\\premade\\allemotions.csv"
  print(s2)
  df = pd.read_csv(s2)
  df = df[df.Emotion==s]
  df2 = df.sample(n=5)
  df3 = df2[['Name','Link']]
  print(df3)

t1 = threading.Thread(target=opencvfunc).start()
t2 = threading.Thread(target=restall).start()


tkinter.mainloop()