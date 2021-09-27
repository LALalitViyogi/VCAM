# importing libraries
import cv2
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

# generating gui kit

main_application = tk.Tk()
main_application.title("V_CAM")
main_application.geometry("660x500")
main_application.minsize(300,350)
main_application.maxsize(700,500)
# Frames 

### main frame
main_frame = tk.Frame(main_application)
main_frame.config(bg='#D5BFF4')
main_frame.pack(fill='both',expand='yes')

## video feed frame
feed_frame = tk.Frame(main_frame)
feed_frame.config(bg='#D7EE98')
feed_frame.pack(padx=5,pady=5,fill='both',expand='yes')

### feed label
feed_label = tk.Label(feed_frame)
feed_label.pack(padx=1,pady=1,fill='both',expand='yes')

video = cv2.VideoCapture(0)
def show_frame():
    feed_image= cv2.cvtColor(video.read()[1],cv2.COLOR_BGR2RGB)
    feed_image = cv2.flip(feed_image,1)
    img = Image.fromarray(feed_image)
    imgtk = ImageTk.PhotoImage(image = img)
    feed_label.imgtk = imgtk
    feed_label.configure(image=imgtk)
    feed_label.after(15, show_frame)
def save_img(event=None):
    print("CLicked")
    #file_url=filedialog.asksaveasfile(mode='wb', defaultextension='.jpeg', filetypes=(('PNG File','*.png'),('JPEG File','*.jpeg'),('All Files','*.*')))
    #file_url.write(feed_label.imgtk)
    #file_url.close()
def quitnow(event=None):
    print("Exiting")
    quit()
feed_label.bind("<Double-Button-1>", save_img)
feed_label.bind("<Double-Button-3>",quitnow)

show_frame()
main_application.mainloop()