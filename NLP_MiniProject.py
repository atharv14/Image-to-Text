#!/usr/bin/env python
# coding: utf-8

# In[64]:


import numpy as np
import tkinter as tk 
from tkinter import *
from tkinter import filedialog
import imageio 
import easygui 
import cv2  
import os
from PIL import Image, ImageTk
import matplotlib.pyplot as plt 
import pytesseract as tess
import sys

top=tk.Tk() 
top.geometry('400x200') 
top.title('Convert Image to Text!!') 
top.configure(background='white') 
label=Label(top,background='#9A9A9A', font=('calibri',20,'bold')) 

def upload_image(): 
    ImagePath=easygui.fileopenbox() 
    get_string(ImagePath) 

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)
    imR = cv2.resize(img, (450, 200)) 
    cv2.imshow('Image', imR)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", img)
    # Recognize text with tesseract for python
    result = tess.image_to_string(Image.open("thres.png"))
    os.remove("thres.png")
    openNewWindow(result)
    
    
def openNewWindow(result):
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(top)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Image to Text")
 
    # sets the geometry of toplevel
    newWindow.geometry("400x200")
    
    #color_coverted = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    #pil_img=Image.fromarray(color_coverted)
    # A Label widget to show in toplevel
    Label(newWindow,text = result).pack()
    
 
 
# a button widget which will open a
# new window on button click
#btn = Button(top,text ="Convert Image to Text",command = openNewWindow)
#btn.pack(pady = 70)

        
upload=Button(top,text="Upload the Image",command=upload_image,padx=10,pady=5) 
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold')) 
upload.pack(side=TOP,pady=50) 

    



top.mainloop()

