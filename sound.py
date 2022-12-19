from tkinter import *
import pygame


w = Tk()
w.title('sound on')
w.geometry('300x300')

pygame.mixer.init()


def play_music():
    pygame.mixer.music.load("C:\\Users\\Manasvi Gaur\\Desktop\\pyproject\\sound.mp3")
    pygame.mixer.music.play(loops=3)

sound_btn = PhotoImage(file="C:\\Users\\\Manasvi Gaur\\Desktop\\pyproject\\sounnd button resize.png")
img_label = Button(w,image=sound_btn,height=19,width=14,command=play_music)


img_label.pack(pady=20)


# sdButton = Button(w,text='play',font=("Helvetica",23),command=play_music)
 # sdButton.pack(pady=10,padx=1)



w.mainloop()