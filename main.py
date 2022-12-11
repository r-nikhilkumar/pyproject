# Packages imported
import random
from tkinter import *
from PIL import ImageTk, Image
# last commit

ls = ['APPLE', 'ABLE', 'ANTIENT', 'ABUSE', 'ABOUT', 'ABOVE', 'ABSENCE', 'ACCESS', 'ACCOUNT', 'ACID', 'ACROSS', 'ACT',
      'ACTOR', 'ACTUAL', 'ADAPT', 'ADJUST', 'ADMIT', 'ADOPT', 'AFTER', 'AFFORD', 'AGAIN', 'AGE', 'AGENT', 'AGREE', 'AHEAD',
      'AIM', 'ALIVE', 'ALLOW', 'ALMOST', 'ALONE', 'LONG', 'ALSO', 'ALWAYS', 'AMONG', 'AMOUNT', 'ANALYZE', 'ANGLE', 'ANIMAL',
      'ANSWER', 'ANY', 'APART', 'APPEAL', 'APPEAR', 'APPLY', 'AREA', 'ARGUE', 'ARISE', 'AROUND', 'ARRANGE', 'ARREST',
      'ART', 'AKS', 'ATTACK', 'AUTO', 'AVOID', 'AWARD', 'AWARE', 'AWAY', 'BABY', 'BACK', 'BAD', 'BAG', 'BAKE', 'BALANCE',
      'BAN', 'BAND', 'BANK', 'BASE', 'BARRIER', 'BASIC', 'BASKET', 'BATTERY', 'BATTLE', 'BEACH', 'BEAR', 'BEAT', 'BECAUSE',
      'BEFORE', 'BEGIN', 'BEHIND', 'BELIEF', 'BELONG', 'BELOW', 'BENEFIT', 'BEST', 'BIKE', 'BIND', 'BIRD', 'BIRTH', 'BLACK',
      'BLAME', 'BLANKET', 'BLIND', 'BLOCK', 'BOARD', 'BOAT', 'BODY', 'BOOK', 'BORDER', 'BORROW', 'BOTHER', 'BOTTLE', 'BOTTOM',
      'BRAIN', 'BREATH', 'BUDGET', 'BUILD', 'BULLET', 'BUSY', 'BUTTON', 'BOYFRIEND', 'BUTTER', 'CABIN', 'CABLE', 'CAKE', 'CALCULATE',
      'CAMERA', 'CAMPUS', 'CANCER', 'CANDIDATE', 'CAPABILITY', 'CAPTAIN', 'CAR', 'CARBON', 'CARD', 'CARRER', 'CAREFUL', 'CARRY',
      'CAT', 'CATCH', 'CAUSE', 'CEILING', 'CELEBRITY', 'CENTER', 'CHAIN', 'CHAIR', 'CHALLENGE', 'CHAMBER', 'CHANGE', 'CHARITY',
      'CHEAP', 'CHECK', 'CHILD', 'CHIP', 'CIRCLE', 'CITY', 'CLAIM', 'DOOR', 'DATE', 'DRINK', 'DINOSAUR', 'DEER', 'DESK', 'DONKEY',
      'DEEP', 'DANCE', 'DUCK', 'DIP', 'DAB', 'DEN', 'DAD', 'DENT', 'DOCK', 'DOG', 'DARK', 'DUST', 'DOWN', 'EGG', 'ELEPHANT', 'ENTER',
      'ENVELOPE', 'EXIT', 'ELEVATOR', 'END', 'ECHO', 'ENGINE', 'EMPTY', 'EAT', 'EAGLE', 'EACH', 'EASY', 'EMAIL', 'EAR', 'EAST',
      'EQUAL', 'ERASE', 'EVEN', 'FALL', 'FRIEND', 'FROG', 'FARM', 'FENCE', 'FIELD', 'FEELING', 'FORK', 'FEET', 'FAN', 'FEED',
      'FELL', 'FEAR', 'FAR', 'FACE', 'FAMILY', 'FAST', 'FAT', 'FIX', 'FIRE', 'GATE', 'GEM', 'GAME', 'GOD','GREAT', 'GOBBLE', 'GUN',
      'GAS', 'GAP', 'GIVE', 'GUM', 'GRAPES', 'GHOST', 'GYM', 'GREEN', 'GRASS', 'GOAT', 'GUITAR', 'GLOVES', 'GENERAL', 'GENERIC',
      'GOAT', 'GLASS', 'GLACIER', 'HIT', 'HOT', 'HAT', 'HUMP', 'HUNGER', 'HAMPER', 'HUNT', 'HAMBURGER', 'HOUSE', 'HOME', 'HIS',
      'HAD', 'HOPE', 'HOPEFUL', 'HEAL', 'HEAT', 'HILL', 'HINT', 'HOP', 'HIP', 'HEEL', 'HEN', 'ICE', 'IDEA', 'IMPORTANT', 'INCREASE',
      'INSIDE', 'INTO', 'INTRODUCE', 'INVENT', 'IRON', 'INVITE', 'IS', 'ISLAND', 'ITEM', 'JACKET', 'JAIL', 'JEWEL',
      'JINGLE', 'JELLYBEAN', 'JOKE', 'JUNE', 'JOYFUL', 'JULY', 'JOLL', 'JETLAG', 'JUGGLING', 'JAGUAR', 'JOURNEY', 'JACKPOT', 'JEWELRY',
      'JUST', 'JELLYFISH', 'JUNCTION', 'KID', 'KEY', 'KIND', 'KOALA', 'KNIT', 'KIWI', 'KICK', 'KING', 'KITTEN', 'KANGAROO',
      'KEYBOARD', 'KITCHEN', 'KNIFE', 'KNIGHT', 'KETCHUP', 'KENNEL', 'KICK', 'KNOT', 'KNEE', 'KITE', 'KNOWLEDGE', 'KNEAD', 'KEEL',
      'KNEW', 'KEEPER', 'KEEP', 'KNOW', 'LADDER', 'LADY', 'LAMP', 'LAND', 'LARGE', 'LAST', 'LATE', 'LATELY', 'LAUGH', 'LAZY', 'LEAD',
      'LEAF', 'LEARN', 'LEAVE', 'LEG', 'LEFT', 'LEND', 'LENGTH', 'LESS', 'LESSON', 'LET', 'LETTER', 'LIBRARY', 'LIE', 'LIFE', 'LIGHT',
      'LIKE', 'LION', 'LIP', 'LIST', 'LISTEN', 'LITTLE', 'LIVE', 'LOCK', 'LONELY', 'LONG', 'LOOK', 'LOSE', 'LOT', 'LOVE', 'LOW',
      'LOWER', 'LUCK', 'MACHINE', 'MAIN', 'MAKE', 'MALE', 'MAN', 'MANY', 'MAP', 'MARK', 'MARKET', 'MARRY', 'MATTER', 'MAY', 'ME',
      'MEAL', 'MEAN', 'MEASURE', 'MEAT', 'MEDICINE', 'MEET', 'MEMBER', 'MENTION', 'METHOD', 'MIDDLE', 'MILK', 'MILLION', 'NAME',
      'NARROW', 'NATION', 'NATURE', 'NEAR', 'NEARLY', 'NECK', 'NEED', 'NEEDLE', 'NEIGHBOUR', 'NEITHER', 'NET', 'NEVER', 'NEW',
      'NEWS', 'NEWSPAPER', 'NEXT', 'NICE', 'NIGHT', 'OBEY', 'OBJECT', 'OCEAN', 'OFFER', 'OFFICE', 'OFTEN', 'OIL',
      'OLD', 'ONE', 'ONLY', 'OPEN', 'OPPOSITE', 'OR', 'ORANGE', 'ORDER', 'OTHER', 'OUR', 'OUT', 'OUTSIDE', 'OVER', 'OWN',
      'PAGE', 'PAIN', 'PAINT', 'PAIR', 'PAN', 'PAPER', 'PARENT', 'PARK', 'PART', 'PARTNER', 'PARTY', 'PASS', 'PAST', 'PATH',
      'PAY', 'PEACE', 'PEN', 'PENCIL', 'PEOPLE', 'PEPPER', 'PER', 'PERFECT', 'PERIOD', 'PERSON', 'PETROL', 'PHOTOGRAPH', 'PIANO',
      'PICK', 'PICTURE', 'PIECE', 'PIG', 'PIN', 'PINK', 'PLACE', 'PLANE', 'PLANT', 'PLASTIC', 'PLATE', 'PLAY', 'PLEASE', 'PLEASED',
      'PLENTY', 'POCKET', 'POINT', 'POISON', 'POLICE', 'POLITE', 'POOL', 'POOR', 'POPULAR', 'POSITION', 'POSSIBLE', 'QUEEN', 'QUESTION',
      'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAIN', 'RAINY', 'RAISE', 'REACH', 'READ', 'READY', 'REAL', 'REALLY', 'RECEIVE', 'RECORD',
      'REMEMBER', 'REMIND', 'REMOVE', 'RENT', 'REPAIR', 'REPEAT', 'REPLY', 'REPORT', 'REST', 'SAD', 'SAFE', 'SAIL', 'SALT', 'SAME',
      'SAVE', 'SAY', 'SCHOOL', 'SCIENCE', 'SCISSORS', 'SEARCH', 'SEAT', 'SECOND', 'SEE', 'SEEM', 'SELL', 'SEND', 'SENTENCE', 'SERVE',
      'SEVEN', 'SEVERAL', 'SHADE', 'SHADOW', 'SHAKE', 'SHAPE', 'SHARE', 'SHARP', 'SHE', 'SHEEP', 'SHEET', 'SHELF', 'SHINE', 'SHIP',
      'SHIRT', 'SHOE', 'SHOOT', 'SHOP', 'SHORT', 'SHOULD', 'SHOULDER', 'SHOUT', 'SHOW', 'SICK', 'SIDE', 'SIGNAL', 'SILENCE', 'SILLY',
      'SILVER', 'SIMILAR', 'SIMPLE', 'SINGLE', 'SINCE', 'SING', 'TABLE', 'TAKE', 'TALK', 'TALL', 'TASTE', 'TAXI', 'TEA', 'TEACH',
      'TEAR', 'TELEPHONE', 'TELEVISION', 'TELL', 'TEN', 'TENNIS', 'TERRIBLE', 'TEST', 'THAN', 'THAT', 'THE', 'THEIR', 'THEN', 'THERE',
      'UGLY', 'UNCLE', 'UNDER', 'UNDERSTAND', 'UNIT', 'UNTIL', 'UP', 'USE', 'USEFUL', 'USUAL', 'USUALLY', 'VEGETABLE', 'VERY',
      'VOICE', 'VISIT', 'WAIT', 'WAKE', 'WALK', 'WANT', 'WARM', 'WAS', 'WASH', 'WASTE', 'WATCH', 'WATER', 'WAY', 'WE', 'WEAK', 'WEAR',
      'WEATHER', 'WEDDING', 'WEEK', 'WEIGHT', 'WELCOME', 'WERE', 'WELL', 'WEST', 'WET', 'WHAT', 'WHEEL', 'XEROX', 'YARD', 'YELL',
      'YET', 'YOU', 'YOUNG', 'YOUR', 'ZERO', 'ZOO', "SHIVAM", "MANASVI", "NIKHIL", "HIMANSHU", "RATAN", "ANSHIKA"]


def choice():
    x = random.choice(ls)
    return x


# def getWord():
wrd = choice()


def jumble(w):
    run = True
    word = ""
    ls = list(w)
    word = word.join(random.sample(w, len(w)))
    return word
word = jumble(wrd)
while word in ls:
    word = jumble(wrd)

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
        st.inputtxt.delete('1.0', 'end')

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

    def hintt():
        hint = []
        y = random.randint(0, len(wrd)-1)
        hint.append("* "*(y))
        hint.append(wrd[y])
        hint.append(" *"*((len(wrd)-1)-y))
        txt = "".join(hint)
        tx = Label(st.start, text=txt, font=(
            "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00")
        tx.place(anchor='w', relx=0.45, rely=0.48)
        
    jum = Label(start, text='The Jumbled Word is:', font=(
        "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00", padx=1, pady=0)
    jum.place(anchor='center', relx=0.3, rely=0.26)
    txt1 = Label(start, text='Enter your guess:', font=(
        "Helvetica", 15, "bold"), bg="#ffe066", fg="#004d00", padx=1, pady=0)
    txt1.place(anchor='center', relx=0.3, rely=0.35)
    i = 2
    # while i>0:
    stText = Label(start, text=f' {word} ', font=(
        "Helvetica", 25, "bold"), bg="#ffe066", fg="#004d00", padx=1, pady=0)
    stText.place(anchor='w', relx=0.45, rely=0.26)
    inputtxt = Text(start, height=1, width=16)
    inputtxt.place(anchor='w', relx=0.45, rely=0.35)
    Submit = Button(start, text="SUBMIT", command=printInput)
    Submit.place(anchor='w', relx=0.45, rely=0.41)
    # wrd = choice()
    # if wrd in ls:
    #     wrd = choice()
    # print(wrd)
    # i-=1
    hint = Button(start, text="❓", command=hintt)
    hint.place(anchor='w', relx=0.53, rely=0.41)


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
