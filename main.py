# Packages imported
import random

import time
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


def choice():
    x = random.choice(ls)
    return x


# def getWord():
# wrd = choice()


def jumble(w):
    run = True
    word = ""
    ls = list(w)
    word = word.join(random.sample(w, len(w)))
    return word
# word = jumble(wrd)
# while word in ls:
    # word = jumble(wrd)

# initializing window:
w = Tk()
w.geometry("800x600")
w.maxsize(800, 600)
loc=os.getcwd()+"\forest.jpeg"
img = ImageTk.PhotoImage(Image.open("forest1.jpeg"))


# creating class for button 'HELP':
class hel:
    help = Frame(w, width=800, height=600)
    help.place(anchor='center', relx=0.5, rely=0.5)
    w.title('HELP')
    # h.pack()
    # Create a Label Widget to display the text or Image
    label3 = Label(help, image=img)

    def helpToHome():
        hel.help.pack_forget()
        home.pack()

    aboutBack = Button(help, text="BACK",
                       font="Helvetica,32", command=helpToHome)
    aboutBack.place(relx=0.5, rely=0.8, anchor=CENTER)

    label3.pack()
    var_text="JUMBLEE is a word puzzle with a clue \nand a set of words ,each of which \nis a 'Jumbled' by scramblings its letters. A Solver reconstructs \nthe words, and them arranges letters at \nmarked positions int the words too \nspell the answer phrase to the clue. The clue and \nsometimes the illustration, provide \nhints about the answer phrase."
    h = Label(help, text=var_text,font=("Helvetica",15,"bold"),bg="#ffe066",fg="Black",padx=0.45,pady=0.45)
    h.place(anchor='w',relx=0.10,rely=0.38)

    def homeToHelp():
        home.pack_forget()
        hel.help.pack()

# creating class for button 'ABOUT':


class ab:
    about = Frame(w, width=800, height=600)
    about.place(anchor='center', relx=0.5, rely=0.5)
    w.title('ABOUT')

    # Create a Label Widget to display the text or Image
    label3 = Label(about, image=img)

    def aboutToHome():
        ab.about.pack_forget()
        home.pack()

    aboutBack = Button(about, text="BACK",
                       font="Helvetica,32", command=aboutToHome)
    aboutBack.place(relx=0.5, rely=0.8, anchor=CENTER)
    label3.pack()

    def homeToAbout():
        home.pack_forget()
        ab.about.pack()

# creating class for button 'START':

class st:
    # w.title('START')
    wrd = choice()
    word = jumble(wrd)
    
    
    def printInput():
        inp = st.inputtxt.get(1.0, "end-1c")
        # Label.config(text =inp)
        # tx = Label(st.start, text=txt, font=(
        #     "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00")
        # tx.place(anchor='w', relx=0.45, rely=0.48)
        if inp.upper() in ls:
            txt = ' Guessed right! '
            st.wrd = choice()
            st.word = jumble(st.wrd)
            st.stText.deletecommand
            st.stText.configure(text=f' {st.word} ')
            #st.tx1.destroy()
            # txt = ""
        else:
            txt = ' Wrong Guess! '
        tx = Label(st.start, text=txt, font=(
            "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00")
        tx.place(anchor='w', relx=0.45, rely=0.48)
        # if txt == ' Guessed right! ':
        #     time.sleep(2)
        #     st.stText.configure(text=f' {st.word} ')
        #     st.tx1.configure(text="")
        #     tx.configure(text="")
        st.inputtxt.delete('1.0', 'end')
        
        # tx.configure(text='')

    start = Frame(w, width=800, height=600)
    label4 = Label(start, image=img)
    label4.pack()
    # start.pack()
    start.place(anchor='center', relx=0.5, rely=0.5)
    # start.wm_attributes('-transparentcolor', '#ab23ff')

    # Create a Label Widget to display the text or Image
    label4 = Label(start, image=img)

    def startToHome():
        st.start.pack_forget()
        home.pack()

    startBack = Button(start, text="BACK",
                       font="Helvetica,32", command=startToHome)
    startBack.place(relx=0.5, rely=0.8, anchor=CENTER)
    label4.pack()

    def homeToStart():
        home.pack_forget()
        st.start.pack()

    # def refresh():
    #     st.start.destroy()
    #     st.start.pack()
    # hint text:
    tx1 = Label(start, font=(
            "Helvetica", 12, "bold"), bg="#ffe066", fg="#004d00")
    tx1.place(anchor='w', relx=0.607, rely=0.41)
    def hintt():
        hint = []
        y = random.randint(0, len(st.wrd)-1)
        hint.append(" * "*(y))
        hint.append(f" {st.wrd[y]} ")
        hint.append(" * "*((len(st.wrd)-1)-y))
        txt = "".join(hint)
        # tx = Label(st.start, font=(
        #     "Helvetica", 12, "bold"), bg="#ffe066", fg="#004d00")
        # tx.place(anchor='w', relx=0.607, rely=0.41)
        st.tx1.configure(text=f" {txt} ")
        
    jum = Label(start, text='The Jumbled Word is:', font=(
        "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00", padx=1, pady=0)
    jum.place(anchor='center', relx=0.3, rely=0.26)
    txt1 = Label(start, text='Enter your guess:', font=(
        "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00", padx=1, pady=0)
    txt1.place(anchor='center', relx=0.3, rely=0.35)
    # i = 2
    # while i>0:
    stText = Label(start, text=f' {word} ', font=(
        "Helvetica", 25, "bold"), bg="#ffe066", fg="#004d00", padx=1, pady=0)
    stText.place(anchor='w', relx=0.45, rely=0.26)
    inputtxt = Text(start, height=1, width=16)
    inputtxt.place(anchor='w', relx=0.45, rely=0.35)
    Submit = Button(start, text="SUBMIT", command=printInput)
    Submit.place(anchor='w', relx=0.45, rely=0.41)
    # time.sleep(2)
    # wrd = choice()
    # if wrd in ls:
    #     wrd = choice()
    # print(wrd)
    # i-=1
    hint = Button(start, text="HINT❓", command=hintt)
    hint.place(anchor='w', relx=0.53, rely=0.41)


# defining HOME frame {main}:

home = Frame(w, width=800, height=600)
home.place(anchor='center', relx=0.5, rely=0.5)
w.title('Jumblee')
# Create a Label Widget to display the text or Image
label = Label(home, image=img)
label.pack()
aboutBut = Button(home, text="ABOUT", font="Helvetica,32",
                  command=ab.homeToAbout)
helpBut = Button(home, text="HELP", font="Helvetica,32",
                 command=hel.homeToHelp)
aboutBut.place(relx=0.5, rely=0.6, anchor=CENTER)
helpBut.place(relx=0.5, rely=0.7, anchor=CENTER)
startBut = Button(home, text="START!!", font="Helvetica,32",
                  command=st.homeToStart)
startBut.place(relx=0.5, rely=0.5, anchor=CENTER)
title = Label(home, text="JUMBLEE",font=("Helvetica",34,"bold"),bg="green",fg="black",padx=1,pady=0)
title.place(anchor=CENTER,relx=0.5,rely=0.1)

home.pack()
i = True
while i:
    st.homeToStart()
    st.startToHome()
    ab.homeToAbout()
    ab.aboutToHome()
    hel.homeToHelp()
    hel.helpToHome()
    i = False
w.mainloop()