# Packages imported
import random
from tkinter import *
from PIL import ImageTk, Image
# last commit


easy=['ABLE', 'ACID', 'ACT', 'AGE', 'AIM', 'LONG', 'ALSO', 'ANY', 'AREA', 'ART', 'AKS', 'AUTO', 'AWAY', 'BABY', 'BACK', 'BAD', 'BAG',
      'BAKE', 'BAN', 'BAND', 'BANK', 'BASE', 'BEAR', 'BEAT', 'BEST', 'BIKE', 'BIND', 'BIRD', 'BOAT', 'BODY', 'BOOK', 'BUSY', 'CAKE', 
      'CAR', 'CARD', 'CAT', 'CHIP', 'CITY', 'DOOR', 'DATE', 'DEER', 'DESK', 'DEEP', 'DUCK', 'DIP', 'DAB', 'DEN', 'DAD', 'DENT', 'DOCK',
      'DOG', 'DARK', 'DUST', 'DOWN', 'EGG', 'EXIT', 'END', 'ECHO', 'EAT', 'EACH', 'EASY', 'EAR', 'EAST', 'EVEN', 'FALL', 'FROG', 'FARM',
      'FORK', 'FEET', 'FAN', 'FEED', 'FELL', 'FEAR', 'FAR', 'FACE', 'FAST', 'FAT', 'FIX', 'FIRE', 'GATE', 'GEM', 'GAME', 'GOD', 'GUN',
      'GAS', 'GAP', 'GIVE', 'GUM', 'GYM', 'GOAT', 'GOAT', 'HIT', 'HOT', 'HAT', 'HUMP', 'HUNT', 'HOME', 'HIS', 'HAD', 'HOPE', 'HEAL',
      'HEAT', 'HILL', 'HINT', 'HOP', 'HIP', 'HEEL', 'HEN', 'ICE', 'IDEA', 'INTO', 'IRON', 'IS', 'ITEM', 'JAIL', 'JOKE', 'JUNE', 'JULY',
      'JOLL', 'JUST', 'KID', 'KEY', 'KIND', 'KNIT', 'KIWI', 'KICK', 'KING', 'KICK', 'KNOT', 'KNEE', 'KITE', 'KEEL', 'KNEW', 'KEEP',
      'KNOW', 'LADY', 'LAMP', 'LAND', 'LAST', 'LATE', 'LAZY', 'LEAD', 'LEAF', 'LEG', 'LEFT', 'LEND', 'LESS', 'LET', 'LIE', 'LIFE',
      'LIKE', 'LION', 'LIP', 'LIST', 'LIVE', 'LOCK', 'LONG', 'LOOK', 'LOSE', 'LOT', 'LOVE', 'LOW', 'LUCK', 'MAIN', 'MAKE', 'MALE',
      'MAN', 'MANY', 'MAP', 'MARK', 'MAY', 'ME', 'MEAL', 'MEAN', 'MEAT', 'MEET', 'MILK', 'NAME', 'NEAR', 'NECK', 'NEED', 'NET', 'NEW',
      'NEWS', 'NEXT', 'NICE', 'OBEY', 'OIL', 'OLD', 'ONE', 'ONLY', 'OPEN', 'OR', 'OUR', 'OUT', 'OVER', 'OWN', 'PAGE', 'PAIN', 'PAIR',
      'PAN', 'PARK', 'PART', 'PASS', 'PAST', 'PATH', 'PAY', 'PEN', 'PER', 'PICK', 'PIG', 'PIN', 'PINK', 'PLAY', 'POOL', 'POOR', 'RAIN',
      'READ', 'REAL', 'RENT', 'REST', 'SAD', 'SAFE', 'SAIL', 'SALT', 'SAME', 'SAVE', 'SAY', 'SEAT', 'SEE', 'SEEM', 'SELL', 'SEND', 'SHE',
      'SHIP', 'SHOE', 'SHOP', 'SHOW', 'SICK', 'SIDE', 'SING', 'TAKE', 'TALK', 'TALL', 'TAXI', 'TEA', 'TEAR', 'TELL', 'TEN', 'TEST',
      'THAN', 'THAT', 'THE', 'THEN', 'UGLY', 'UNIT', 'UP', 'USE', 'VERY', 'WAIT', 'WAKE', 'WALK', 'WANT', 'WARM', 'WAS', 'WASH', 'WAY',
      'WE', 'WEAK', 'WEAR', 'WEEK', 'WERE', 'WELL', 'WEST', 'WET', 'WHAT', 'YARD', 'YELL', 'YET', 'YOU', 'YOUR', 'ZERO', 'ZOO']




medium=['APPLE', 'ABUSE', 'ABOUT', 'ABOVE', 'ACCESS', 'ACROSS', 'ACTOR', 'ACTUAL', 'ADAPT', 'ADJUST', 'ADMIT', 'ADOPT', 'AFTER',
        'AFFORD', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALIVE', 'ALLOW', 'ALMOST', 'ALONE', 'ALWAYS', 'AMONG', 'AMOUNT', 'ANGLE',
        'ANIMAL', 'ANSWER', 'APART', 'APPEAL', 'APPEAR', 'APPLY', 'ARGUE', 'ARISE', 'AROUND', 'ARREST', 'ATTACK', 'AVOID', 'AWARD',
        'AWARE', 'BASIC', 'BASKET', 'BATTLE', 'BEACH', 'BEFORE', 'BEGIN', 'BEHIND', 'BELIEF', 'BELONG', 'BELOW', 'BIRTH', 'BLACK',
        'BLAME', 'BLIND', 'BLOCK', 'BOARD', 'BORDER', 'BORROW', 'BOTHER', 'BOTTLE', 'BOTTOM', 'BRAIN', 'BREATH', 'BUDGET', 'BUILD',
        'BULLET', 'BUTTON', 'BUTTER', 'CABIN', 'CABLE', 'CAMERA', 'CAMPUS', 'CANCER', 'CARBON', 'CARRER', 'CARRY', 'CATCH', 'CAUSE',
        'CENTER', 'CHAIN', 'CHAIR', 'CHANGE', 'CHEAP', 'CHECK', 'CHILD', 'CIRCLE', 'CLAIM', 'DRINK', 'DONKEY', 'DANCE', 'ENTER',
        'ENGINE', 'EMPTY', 'EAGLE', 'EMAIL', 'EQUAL', 'ERASE', 'FRIEND', 'FENCE', 'FIELD', 'FAMILY', 'GREAT', 'GOBBLE', 'GRAPES',
        'GHOST', 'GREEN', 'GRASS', 'GUITAR', 'GLOVES', 'GLASS', 'HUNGER', 'HAMPER', 'HOUSE', 'INSIDE', 'INVENT', 'INVITE', 'ISLAND',
        'JACKET', 'JEWEL', 'JINGLE', 'JOYFUL', 'JETLAG', 'JAGUAR', 'KOALA', 'KITTEN', 'KNIFE', 'KNIGHT', 'KENNEL', 'KNEAD', 'KEEPER',
        'LADDER', 'LARGE', 'LATELY', 'LAUGH', 'LEARN', 'LEAVE', 'LENGTH', 'LESSON', 'LETTER', 'LIGHT', 'LISTEN', 'LITTLE', 'LONELY',
        'LOWER', 'MARKET', 'MARRY', 'MATTER', 'MEMBER', 'METHOD', 'MIDDLE', 'NARROW', 'NATION', 'NATURE', 'NEARLY', 'NEEDLE', 'NEVER',
        'NIGHT', 'OBJECT', 'OCEAN', 'OFFER', 'OFFICE', 'OFTEN', 'ORANGE', 'ORDER', 'OTHER', 'PAINT', 'PAPER', 'PARENT', 'PARTY',
        'PEACE', 'PENCIL', 'PEOPLE', 'PEPPER', 'PERIOD', 'PERSON', 'PETROL', 'PIANO', 'PIECE', 'PLACE', 'PLANE', 'PLANT', 'PLATE',
        'PLEASE', 'PLENTY', 'POCKET', 'POINT', 'POISON', 'POLICE', 'POLITE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAINY',
        'RAISE', 'REACH', 'READY', 'REALLY', 'RECORD', 'REMIND', 'REMOVE', 'REPAIR', 'REPEAT', 'REPLY', 'REPORT', 'SCHOOL', 'SEARCH',
        'SECOND', 'SERVE', 'SEVEN', 'SHADE', 'SHADOW', 'SHAKE', 'SHAPE', 'SHARE', 'SHARP', 'SHEEP', 'SHEET', 'SHELF', 'SHINE', 'SHIRT',
        'SHOOT', 'SHORT', 'SHOULD', 'SHOUT', 'SIGNAL', 'SILLY', 'SILVER', 'SIMPLE', 'SINGLE', 'SINCE', 'TABLE', 'TASTE', 'TEACH',
        'TENNIS', 'THEIR', 'THERE', 'UNCLE', 'UNDER', 'UNTIL', 'USEFUL', 'USUAL', 'VOICE', 'VISIT', 'WASTE', 'WATCH', 'WATER',
        'WEIGHT', 'WHEEL', 'XEROX', 'YOUNG', 'SHIVAM', 'NIKHIL', 'RATAN']




hard=['ANTIENT', 'ABSENCE', 'ACCOUNT', 'ANALYZE', 'ARRANGE', 'BALANCE', 'BARRIER', 'BATTERY', 'BECAUSE', 'BENEFIT', 'BLANKET',
      'BOYFRIEND', 'CALCULATE', 'CANDIDATE', 'CAPABILITY', 'CAPTAIN', 'CAREFUL', 'CEILING', 'CELEBRITY', 'CHALLENGE', 'CHAMBER',
      'CHARITY', 'DINOSAUR', 'ELEPHANT', 'ENVELOPE', 'ELEVATOR', 'FEELING', 'GENERAL', 'GENERIC', 'GLACIER', 'HAMBURGER', 'HOPEFUL',
      'IMPORTANT', 'INCREASE', 'INTRODUCE', 'JELLYBEAN', 'JUGGLING', 'JOURNEY', 'JACKPOT', 'JEWELRY', 'JELLYFISH', 'JUNCTION',
      'KANGAROO', 'KEYBOARD', 'KITCHEN', 'KETCHUP', 'KNOWLEDGE', 'LIBRARY', 'MACHINE', 'MEASURE', 'MEDICINE', 'MENTION', 'MILLION',
      'NEIGHBOUR', 'NEITHER', 'NEWSPAPER', 'OPPOSITE', 'OUTSIDE', 'PARTNER', 'PERFECT', 'PHOTOGRAPH', 'PICTURE', 'PLASTIC', 'PLEASED',
      'POPULAR', 'POSITION', 'POSSIBLE', 'QUESTION', 'RECEIVE', 'REMEMBER', 'SCIENCE', 'SCISSORS', 'SENTENCE', 'SEVERAL', 'SHOULDER',
      'SILENCE', 'SIMILAR', 'TELEPHONE', 'TELEVISION', 'TERRIBLE', 'UNDERSTAND', 'USUALLY', 'VEGETABLE', 'WEATHER', 'WEDDING',
      'WELCOME', 'MANASVI', 'HIMANSHU', 'ANSHIKA']



def choice():
    x = random.choice(medium)
    return x


# def getWord():

def jumble(w):
    run = True
    word = ""
    medium = list(w)
    word = word.join(random.sample(w, len(w)))
    return word


wrd = choice()
word = jumble(wrd)
while word in medium:
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

# creating class for button 'START':

class st:
    # w.title('START')

    def printInput():
        inp = st.inputtxt.get(1.0, "end-1c")
        # Label.config(text =inp)

        if inp.upper() in ls:
            txt = ' Guessed right! '
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

    # def refresh():
    #     st.start.destroy()
    #     st.start.pack()

    def hintt():
        hint = []
        y = random.randint(0, len(wrd)-1)
        hint.append("* "*(y))
        hint.append(wrd[y])
        hint.append(" *"*((len(wrd)-1)-y))
        txt = "".join(hint)
        tx = Label(st.start, text=txt, font=(
            "Helvetica", 12, "bold"), bg="#ffe066", fg="#004d00")
        tx.place(anchor='w', relx=0.607, rely=0.41)
        
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
    # if wrd in medium:
    #     wrd = choice()
    # print(wrd)
    # i-=1
    hint = Button(start, text="HINT❓")
    hint.place(anchor='w', relx=0.53, rely=0.41)
    hint.configure(command=hintt)


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