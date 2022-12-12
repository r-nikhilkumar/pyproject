# Packages imported
import random
from tkinter import *
from PIL import ImageTk, Image

# declaring word list:
import os
 
#location of file
location=os.getcwd()
location=os.getcwd()+"\words\words.txt"

#opening file
fo=open(location,'r')
# print(fo.read())
L=fo.read()
# print(L)
L.split(',')
ls=eval(L)

#picking random word
def choice():
    x = random.choice(ls)
    return x

#unshuffle word
word=choice()

#shuffle the word
def jumble(w):
    run = True
    word = ""
    ls = list(w)
    word = word.join(random.sample(w, len(w)))
    return word
word = jumble(word)

# initailizing windows
w = Tk()
w.geometry("800x600")
w.maxsize(800, 600)
loc=os.getcwd()+"\forest.jpeg"
img = ImageTk.PhotoImage(Image.open("forest1.jpeg"))
w.mainloop()