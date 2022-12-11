#jaishreeganesh
#jaishreeram
import random
from tkinter import*
from PIL import Image, ImageTk
import time

ls = ["APPLE","ABLE","ANTIENT","ABUSE","ABOUT","ABOVE","ABSENCE","ACCESS","ACCOUNT","ACID","ACROSS","ACT",
    "ACTOR","ACTUAL","ADAPT","ADJUST","ADMIT","ADOPT","AFTER","AFFORD","AGAIN","AGE","AGENT","AGREE","AHEAD",
    "AIM","ALIVE","ALLOW","ALMOST","ALONE","ALONG","ALSO","ALWAYS","AMONG","AMOUNT","ANALYZE","ANGLE","ANIMAL",
    "ANSWER","ANY","APART","APPEAL","APPEAR","APPLY","AREA","ARGUE","ARISE","AROUND","ARRANGE","ARREST",
    "ART","AKS","ATTACK","AUTO","AVOID","AWARD","AWARE","AWAY","BABY","BACK","BAD","BAG","BAKE","BALANCE",
    "BAN","BAND","BANK","BASE","BARRIER","BASIC","BASKET","BATTERY","BATTLE","BEACH","BEAR","BEAT","BECAUSE",
    "BEFORE","BEGIN","BEHIND","BELIEF","BELONG","BELOW","BENEFIT","BEST","BIKE","BIND","BIRD","BIRTH","BLACK",
    "BLAME","BLANKET","BLIND","BLOCK","BOARD","BOAT","BODY","BOOK","BORDER","BORROW","BOTHER","BOTTLE","BOTTOM",
    "BRAIN","BREATH","BUDGET","BUILD","BULLET","BUSY","BUTTON","BOYFRIEND","BUTTER","CABIN","CABLE","CAKE","CALCULATE",
    "CAMERA","CAMPUS","CANCER","CANDIDATE","CAPABILITY","CAPTAIN","CAR","CARBON","CARD","CARRER","CAREFUL","CARRY","CASE","CASH",
    "CAT","CATCH","CAUSE","CEILING","CELEBRITY","CENTER","CHAIN","CHAIR","CHALLENGE","CHAMBER","CHANGE","CHARITY","CHASE",
    "CHEAP","CHECK","CHILD","CHIP","CIRCLE","CITY","CLAIM","ANSHIKA","NIKHIL","SHIVAM","MANASVI","HIMANSHU","RATAN"]


def choice():
    x = random.choice(ls)
    return x
wrd = choice()
if wrd in ls:
    wrd = choice()

def jumble(w):
    w=list(w)
    print(w)
    random.shuffle(w)
    k=''
    k=k.join(w)
    return k

def printInput():
    inp = inputtxt.get(1.0, "end-1c")

    # Label.config(text =inp)

    if inp.upper() in ls:
        txt= 'You Guessed right!'
    else:
        txt = 'Wrong Guess!'
    w.after(1000)
    tx = Label(start,text=txt,font=("Helvetica",15,"bold"),bg="#ffe066",fg="#004d00")
    tx.place(anchor='w',relx=0.45,rely=0.48)
    inputtxt.delete("1.0", "end")

while True:
    w = Tk()
    w.geometry('800x600')
    # global entry
    img = ImageTk.PhotoImage(Image.open('forest1.jpeg'))
    start = Frame(w, width=800,height=600)
    label4 = Label(start, image=img)
    label4.pack()
    start.pack()
    start.place(anchor='center', relx=0.5, rely=0.5)
    # start.wm_attributes('-transparentcolor', '#ab23ff')
    jum = Label(start,text='The Jumbled Word is:',font=("Helvetica",15,"bold"),bg="#ffe066",fg="#004d00",padx=1,pady=0)
    jum.place(anchor='center',relx=0.3,rely=0.26)
    stText = Label(start,text=f' {jumble(wrd)} ',font=("Helvetica",25,"bold"),bg="#ffe066",fg="#004d00",padx=1,pady=0)
    stText.place(anchor='w',relx=0.45,rely=0.26)
    txt1 = Label(start,text='Enter your guess:',font=("Helvetica",15,"bold"),bg="#ffe066",fg="#004d00",padx=1,pady=0)
    txt1.place(anchor='center',relx=0.3,rely=0.35)
    inputtxt = Text(start,height = 1,width = 16)
    inputtxt.place(anchor='w',relx=0.45,rely=0.35)
    printButton = Button(start,text = "SUBMIT",command = printInput)
    printButton.place(anchor='w',relx=0.45,rely=0.41)
    # printButton.pack()

    

    # string = entry.get()

    # head=Label(w,text="JUMBLEE",font=("Helvetica",34,"bold"),bg="green",fg="black",padx=1,pady=0)
    # stText.pack()


    w.mainloop()