# Packages imported
import random
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer


# declaring word list:
import os
#function to play click sound:
def click_sound():
    mixer.init()
    mixer.music.load("click.mp3")
    mixer.music.play()
 
#location of file
location=os.getcwd()
location=os.getcwd()+"//words//words.txt"

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
def jumble(w):
    run = True
    word = ""
    ls = list(w)
    word = word.join(random.sample(w, len(w)))
    if word == w:
        return jumble(w)
    return word


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
    imgHelp = ImageTk.PhotoImage(Image.open("helpImg.jpeg"))
    label3 = Label(help, image=imgHelp)

    def helpToHome():
        hel.help.pack_forget()
        home.pack()
        click_sound()

    aboutBack = Button(help, text="BACK",font="Helvetica,32", command=helpToHome)
    aboutBack.place(relx=0.5, rely=0.8, anchor=CENTER)

    label3.pack()
    
    def homeToHelp():
        home.pack_forget()
        hel.help.pack()
        click_sound()

# creating class for button 'ABOUT':


class ab:
    about = Frame(w, width=800, height=600)
    about.place(anchor='center', relx=0.5, rely=0.5)
    w.title('ABOUT')

    # Create a Label Widget to display the text or Image
    imgAb = ImageTk.PhotoImage(Image.open("aboutImg.jpeg"))
    label3 = Label(about, image=imgAb)

    def aboutToHome():
        ab.about.pack_forget()
        home.pack()
        click_sound()

    aboutBack = Button(about, text="BACK",
                       font="Helvetica,32", command=aboutToHome)
    aboutBack.place(relx=0.5, rely=0.8, anchor=CENTER)
    label3.pack()
    
    def homeToAbout():
        home.pack_forget()
        ab.about.pack()
        click_sound()



# creating class for button 'START':



def quit():
        st.start.pack_forget()
        scr = Frame(w, width=800, height=600)
        # w.maxsize()
        # scr.pack()
        # Create a Label Widget to display the text or Image
        label = Label(scr, image = img)
        var_text="SCOREBOARD"
        scr.place(anchor='center', relx=0.5, rely=0.5)
        w.title('scoreboard')
        label.place(anchor=CENTER,relx=0.5,rely=0.5)
        label.pack()
        scrT = Label(scr,text=var_text,font=("Helvetica",10,"bold"),bg="#ffe066",fg="Black",padx=1,pady=0)
        scrT.place(anchor='c',relx=0.5,rely=0.15)
        # scrT.pack()
    
        scr.pack()





class st:
    # w.title('START')
    wrd = choice()
    word = jumble(wrd)
    hintNo = 0
    score = 0
    hintRed = 0
    def printInput():
        inp = st.inputtxt.get(1.0, "end-1c")
        # Label.config(text =inp)

        if inp.upper() in ls:
            txt = ' Guessed right! '
            st.wrd = choice()
            st.word = jumble(st.wrd)
            st.stText.configure(text=f' {st.word} ')
            mixer.init()
            mixer.music.load("correct.mp3")
            mixer.music.play()
            st.hintNo = 0
            st.txh.configure(text="")
            st.score+=10+st.hintRed
            st.hintRed=0
            st.scL.configure(text=f'SCORE: {st.score}')
        else:
            txt = ' Wrong Guess! '
            mixer.init()
            mixer.music.load("wrong.mp3")
            mixer.music.play()
        tx = Label(st.start, text=txt, font=(
            "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00")
        tx.place(anchor='w', relx=0.45, rely=0.48)
        st.inputtxt.delete('1.0', 'end')

    start = Frame(w, width=800, height=600)
    label4 = Label(start, image=img)
    label4.pack()
    # start.pack()
    start.place(anchor='center', relx=0.5, rely=0.5)
    # start.wm_attributes('-transparentcolor', '#ab23ff')

    # Create a Label Widget to display the text or Image
    label4 = Label(start, image=img)
    scL = Label(start, text=f'SCORE: {score}', font=(
            "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00")
    scL.place(anchor='c',relx=0.8,rely=0.1)
    def startToHome():
        st.start.pack_forget()
        home.pack()
        click_sound()

    startBack = Button(start, text="BACK",
                       font="Helvetica,32", command=startToHome)
    startBack.place(relx=0.5, rely=0.8, anchor=CENTER)
    label4.pack()

    def homeToStart():
        home.pack_forget()
        st.start.pack()
        click_sound()

    # def refresh():
    #     st.start.destroy()
    #     st.start.pack()
    
    txh = Label(start, font=(
            "Helvetica", 12, "bold"), bg="#ffe066", fg="#004d00")
    txh.place(anchor='w', relx=0.607, rely=0.41)
    
    def hintt():
        hint = []
        y = random.randint(0, len(st.wrd)-1)
        hint.append("* "*(y))
        hint.append(st.wrd[y])
        hint.append(" *"*((len(st.wrd)-1)-y))
        txt = "".join(hint)
        
        mixer.init()
        mixer.music.load("hint.mp3")
        mixer.music.play()
        if st.hintNo<3:
            st.txh.configure(text=f" {txt} ")
            st.hintNo+=1
            st.hintRed-=2
        else:
            st.txh.configure(text="You can't use hint anymore!")
        
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
    
    goToSc = Button(start, text="QUIT", command=quit)
    goToSc.place(anchor='c', relx=0.5, rely=0.65)
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


startBut = Button(home, text="START!!", font="Helvetica,32",command=st.homeToStart)
startBut.place(relx=0.5, rely=0.5, anchor=CENTER)
# BINDING ENTER KEY:
st.start.bind('<Return>',st.printInput)




title = Label(home, text="JUMBLEE",font=("Helvetica",25,"bold"),bg="#ffe066", fg="#004d00",padx=1,pady=0)
title.place(anchor=CENTER,relx=0.5,rely=0.1)


#for background sound:

def play_music():
    mixer.init()
    mixer.music.load("sound.mp3")
    if button["text"] == "\U0001F507":
        button["text"] = "\U0001F508"
        button["bg"] = "green"
        mixer.music.play()
    else:
        button["text"] = "\U0001F507"
        button["bg"] = "orange"
        mixer.music.pause()

button = Button(w, text="\U0001F507",font=("Arial",15,"bold"), width=2, bg='green', fg='black', command=play_music)
button.place(relx=0.92,rely=0.05)

loginF = Frame(w, width=800, height=600)
l_label=Label(loginF, image=img)
l_label.place(relx=0,rely=0)
title = Label(loginF, text="JUMBLEE",font=("Helvetica",25,"bold"),bg="#ffe066", fg="#004d00",padx=1,pady=0)
title.place(anchor=CENTER,relx=0.5,rely=0.1)
# method to make loginButton Functional:
def log():
    click_sound()
    loginF.pack_forget()
    home.pack()
    fName = EnterFName.get(1.0, "end-1c")
    # lName = EnterLName.get(1.0, "end-1c")
    showname = Label(home, text=f"Welcome,\n{fName}",font=('bold',16))
    showname.place(relx=0.5,rely=0.33,anchor='c')


EnterFName = Text(loginF, height=1,width=9,font=('bold',20))
EnterName = Label(loginF, text="Enter Your Name:",font=("Helvetica",20,"bold"),bg="yellow")
# w.wm_attributes('-transparentcolor', 'yellow')
EnterFName.place(anchor='c',relx= 0.61,rely=0.37)
EnterName.place(anchor='c',relx= 0.35,rely=0.37)
loginButton = Button(loginF, text="Login", command=log)
loginButton.place(relx=0.5,rely=0.5,anchor=CENTER)
    


# home.pack()
loginF.pack()
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
