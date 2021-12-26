# importing libraries
import cv2
#from cv2.cv import dnn_superres
import tkinter as tk
from tkinter import filedialog
import os
import datetime
from PIL import Image, ImageTk

# generating gui kit

main_application = tk.Tk()
main_application.title("V_CAM")
main_application.geometry("660x530")
main_application.minsize(630,520)
main_application.maxsize(660,530)
main_application.iconbitmap('./images/logo_s.ico')
# Frames 

### main frame
main_frame = tk.Frame(main_application)
main_frame.config(bg='#D5BFF4')
main_frame.grid(row=0,column=0)

but_frame = tk.Frame(main_application)
but_frame.config(bg='#f0f0f0')
but_frame.grid(column=0,row=2)

## video feed frame
feed_frame = tk.Frame(main_frame)
feed_frame.config(bg='#D7EE98')
feed_frame.pack(padx=3)



### feed label
feed_label = tk.Label(feed_frame)
feed_label.pack(padx=1)

video = cv2.VideoCapture(0)
#sr = cv2.dnn_superres.DnnSuperResImpl_create()

path = "EDSR_x3.pb"
#sr.readModel(path)
#sr.setModel("edsr", 3)

saved = False
entry_open= False

def show_frame():
    feed_image= cv2.cvtColor(video.read()[1],cv2.COLOR_BGR2RGB)
    feed_image = cv2.flip(feed_image,1)
    #dst = cv2.detailEnhance(feed_image, sigma_s=150, sigma_r=0.99)
    #result = sr.upsample(feed_image)
    img = Image.fromarray(feed_image)
    imgtk = ImageTk.PhotoImage(image = img)
    feed_label.imgtk = imgtk
    feed_label.configure(image=imgtk)
    feed_label.after(15, show_frame)
def save_img(event=None):
    #global saved,entry_open
    image =ImageTk.getimage(feed_label.imgtk)
    #image = feed_label.imgtk
    time = datetime.datetime.now()
    image_path = os.getcwd()+"\\photos"
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    path = os.path.join(image_path,"IMG_"+str(time.year)+str(time.month)+"_"+str(time.day)+"_"+str(time.hour)+str(time.minute)+str(time.second)+".png")
    image.save(path,'PNG')
    image.close()
def exit_func(event=None):
    quit()



############################ BUttons Section
## buttons 
click_btn = tk.Button(but_frame,command=save_img)
click_btn.config(height=2,width=30,text="save")
click_btn.pack(side=tk.LEFT)
#feed_label.bind("<Double-Button-1>", save_img)
feed_label.bind("<Double-Button-3>",exit_func)

### window protocol event handelling
main_application.protocol("WM_DELETE_WINDOW",exit_func)

show_frame()
main_application.mainloop()