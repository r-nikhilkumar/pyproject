# Packages imported
import random
from tkinter import *
from PIL import ImageTk, Image
# last commit

ls = ["APPLE", "ABLE", "ANTIENT", "ABUSE", "ABOUT", "ABOVE", "ABSENCE", "ACCESS", "ACCOUNT", "ACID", "ACROSS", "ACT",
      "ACTOR", "ACTUAL", "ADAPT", "ADJUST", "ADMIT", "ADOPT", "AFTER", "AFFORD", "AGAIN", "AGE", "AGENT", "AGREE", "AHEAD",
      "AIM", "ALIVE", "ALLOW", "ALMOST", "ALONE", "ALONG", "ALSO", "ALWAYS", "AMONG", "AMOUNT", "ANALYZE", "ANGLE", "ANIMAL",
      "ANSWER", "ANY", "APART", "APPEAL", "APPEAR", "APPLY", "AREA", "ARGUE", "ARISE", "AROUND", "ARRANGE", "ARREST",
      "ART", "AKS", "ATTACK", "AUTO", "AVOID", "AWARD", "AWARE", "AWAY", "BABY", "BACK", "BAD", "BAG", "BAKE", "BALANCE",
      "BAN", "BAND", "BANK", "BASE", "BARRIER", "BASIC", "BASKET", "BATTERY", "BATTLE", "BEACH", "BEAR", "BEAT", "BECAUSE",
      "BEFORE", "BEGIN", "BEHIND", "BELIEF", "BELONG", "BELOW", "BENEFIT", "BEST", "BIKE", "BIND", "BIRD", "BIRTH", "BLACK",
      "BLAME", "BLANKET", "BLIND", "BLOCK", "BOARD", "BOAT", "BODY", "BOOK", "BORDER", "BORROW", "BOTHER", "BOTTLE", "BOTTOM",
      "BRAIN", "BREATH", "BUDGET", "BUILD", "BULLET", "BUSY", "BUTTON", "BOYFRIEND", "BUTTER", "CABIN", "CABLE", "CAKE", "CALCULATE",
      "CAMERA", "CAMPUS", "CANCER", "CANDIDATE", "CAPABILITY", "CAPTAIN", "CAR", "CARBON", "CARD", "CARRER", "CAREFUL", "CARRY", "CASE", "CASH",
      "CAT", "CATCH", "CAUSE", "CEILING", "CELEBRITY", "CENTER", "CHAIN", "CHAIR", "CHALLENGE", "CHAMBER", "CHANGE", "CHARITY", "CHASE",
      "CHEAP", "CHECK", "CHILD", "CHIP", "CIRCLE", "CITY", "CLAIM", "ANSHIKA", "NIKHIL", "SHIVAM", "MANASVI", "HIMANSHU", "RATAN"]


def choice():
    x = random.choice(ls)
    return x


wrd = choice()
if wrd in ls:
    wrd = choice()


def jumble(w):
    ls = []
    run = True
    word = ""
    while run:
        while True:
            x = random.randint(0, len(w)-1)
            if x not in ls:
                ls.append(x)
            if len(ls) == len(w):
                break

        word = ""
        for i in ls:
            word += w[i]+" "
        if word != w:
            run = False
    # print(ls)
    return word


# initializing window:
w = Tk()
w.geometry("800x600")
w.maxsize(800, 600)
img = ImageTk.PhotoImage(Image.open('forest1.jpeg'))


# creating class for button 'HELP':
class hel:
    help = Frame(w, width=800, height=600)
    help.place(anchor='center', relx=0.5, rely=0.5)
    w.title('HELP')

    # Create a Label Widget to display the text or Image
    label3 = Label(help, image=img)

    def helpToHome():
        hel.help.pack_forget()
        home.pack()

    aboutBack = Button(help, text="BACK",
                       font="Helvetica,32", command=helpToHome)
    aboutBack.place(relx=0.5, rely=0.8, anchor=CENTER)

    label3.pack()

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


class st:
    # w.title('START')

    def printInput():
        inp = st.inputtxt.get(1.0, "end-1c")
        # Label.config(text =inp)

        if inp.upper() in ls:
            txt = 'You Guessed right!'
        else:
            txt = 'Wrong Guess!'
        tx = Label(st.start, text=txt, font=(
            "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00")
        tx.place(anchor='w', relx=0.45, rely=0.48)
        st.inputtxt.delete('1.0','end')

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
    def refreshfun():
        st.start.destroy()
        st.start.pack()

    jum = Label(start, text='The Jumbled Word is:', font=(
        "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00", padx=1, pady=0)
    jum.place(anchor='center', relx=0.3, rely=0.26)
    txt1 = Label(start, text='Enter your guess:', font=(
        "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00", padx=1, pady=0)
    txt1.place(anchor='center', relx=0.3, rely=0.35)

    stText = Label(start, text=f' {jumble(wrd)} ', font=(
        "Helvetica", 25, "bold"), bg="#ffe066", fg="#004d00", padx=1, pady=0)
    stText.place(anchor='w', relx=0.45, rely=0.26)
    inputtxt = Text(start, height=1, width=16)
    inputtxt.place(anchor='w', relx=0.45, rely=0.35)
    Submit = Button(start, text="SUBMIT", command=printInput)
    Submit.place(anchor='w', relx=0.45, rely=0.41)
    refresh = Button(start, text="REFRESH", command=refreshfun)
    refresh.place(anchor='w', relx=0.53, rely=0.41)
    

# defining frame 1:


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
