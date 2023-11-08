from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()

root= Tk()
root.geometry("2000x800")

def play_gif():
   root.lift()
   root.attributes("-topmost",True)
   global image
   img=Image.open("download.gif")
    
   label=Label(root)
   label.place(x=0,y=0)
   i=0

   mixer.music.load("CompFuturing.mp3")
   mixer.music.play()
    
   for img in ImageSequence.Iterator(img):
        img=img.resize((2000,800))
        img=ImageTk.PhotoImage(img)
        label.config(image=img)
        root.update()
        time.sleep(0.05)
    
   root.destroy()

play_gif()
root.mainloop()
