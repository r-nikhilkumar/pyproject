import random
# import time


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
      'DEEP', 'DANCE', 'DUCK', 'DIP', 'DAB', 'DEN', 'DAD', 'DENT', 'DOCK', 'DARK', 'DUST', 'DOWN', 'EGG', 'ELEPHANT', 'ENTER',
      'ENVELOPE', 'EXIT', 'ELEVATOR', 'END', 'ECHO', 'ENGINE', 'EMPTY', 'EAT', 'EAGLE', 'EACH', 'EASY', 'EMAIL', 'EAR', 'EAST',
      'EQUAL', 'ERASE', 'EVEN', 'FALL', 'FRIEND', 'FROG', 'FARM', 'FENCE', 'FIELD', 'FEELING', 'FORK', 'FEET', 'FAN', 'FEED',
      'FELL', 'FEAR', 'FAR', 'FACE', 'FAMILY', 'FAST', 'FAT', 'FIX', 'FIRE', 'GATE', 'GEM', 'GAME', 'GREAT', 'GOBBLE', 'GUN',
      'GAS', 'GAP', 'GIVE', 'GUM', 'GRAPES', 'GHOST', 'GYM', 'GREEN', 'GRASS', 'GOAT', 'GUITAR', 'GLOVES', 'GENERAL', 'GENERIC',
      'GOAT', 'GLASS', 'GLACIER', 'HIT', 'HOT', 'HAT', 'HUMP', 'HUNGER', 'HAMPER', 'HUNT', 'HAMBURGER', 'HOUSE', 'HOME', 'HIS',
      'HAD', 'HOPE', 'HOPEFUL', 'HEAL', 'HEAT', 'HILL', 'HINT', 'HOP', 'HIP', 'HEEL', 'HEN', 'ICE', 'IDEA', 'IMPORTANT', 'INCREASE',
      'INSIDE', 'INTO', 'INTRODUCE', 'INVENT', 'IRON', 'INVITE', 'IS', 'ISLAND', 'ITEM', 'JACKET', 'JAIL', 'JAM', '', 'JET', 'JEWEL',
      'JINGLE', 'JELLYBEAN', 'JOKE', 'JUNE', 'JOYFUL', 'JULY', 'JOLL', 'JETLAG', 'JUGGLING', 'JAGUAR', 'JOURNEY', 'JACKPOT', 'JEWELRY',
      'JUST', 'JELLYFISH', 'JUNCTION', 'KID', 'KEY', 'KIND', 'KOALA', 'KNIT', 'KIWI', 'KICK', 'KING', 'KIT', 'KITTEN', 'KANGAROO',
      'KEYBOARD', 'KITCHEN', 'KNIFE', 'KNIGHT', 'KETCHUP', 'KENNEL', 'KICK', 'KNOT', 'KNEE', 'KITE', 'KNOWLEDGE', 'KNEAD', 'KEEL',
      'KNEW', 'KEEPER', 'KEEP', 'KNOW', 'LADDER', 'LADY', 'LAMP', 'LAND', 'LARGE', 'LAST', 'LATE', 'LATELY', 'LAUGH', 'LAZY', 'LEAD',
      'LEAF', 'LEARN', 'LEAVE', 'LEG', 'LEFT', 'LEND', 'LENGTH', 'LESS', 'LESSON', 'LET', 'LETTER', 'LIBRARY', 'LIE', 'LIFE', 'LIGHT',
      'LIKE', 'LION', 'LIP', 'LIST', 'LISTEN', 'LITTLE', 'LIVE', 'LOCK', 'LONELY', 'LONG', 'LOOK', 'LOSE', 'LOT', 'LOVE', 'LOW',
      'LOWER', 'LUCK', 'MACHINE', 'MAIN', 'MAKE', 'MALE', 'MAN', 'MANY', 'MAP', 'MARK', 'MARKET', 'MARRY', 'MATTER', 'MAY', 'ME',
      'MEAL', 'MEAN', 'MEASURE', 'MEAT', 'MEDICINE', 'MEET', 'MEMBER', 'MENTION', 'METHOD', 'MIDDLE', 'MILK', 'MILLION', 'NAME',
      'NARROW', 'NATION', 'NATURE', 'NEAR', 'NEARLY', 'NECK', 'NEED', 'NEEDLE', 'NEIGHBOUR', 'NEITHER', 'NET', 'NEVER', 'NEW',
      'NEWS', 'NEWSPAPER', 'NEXT', 'NICE', 'NIGHT', 'OBEY', 'OBJECT', 'OCEAN', 'OF', 'OFF', 'OFFER', 'OFFICE', 'OFTEN', 'OIL',
      'OLD', 'ON', 'ONE', 'ONLY', 'OPEN', 'OPPOSITE', 'OR', 'ORANGE', 'ORDER', 'OTHER', 'OUR', 'OUT', 'OUTSIDE', 'OVER', 'OWN',
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
      'YET', 'YOU', 'YOUNG', 'YOUR', 'ZERO', 'ZOO', "ANSHIKA", "NIKHIL", "SHIVAM", "MANASVI", "HIMANSHU", "RATAN"]


def choice():
    x = random.choice(ls)
    return x


# def jumble(word):
#     y = random.sample(word, len(word))
#     jumbled = "".join(y)
#     return jumbled
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


def play():
    player1 = input("Enter your name: ").upper()
#     player2=input("Enter your name: ")
    score = 0
    hint = []
    for i in range(5):
        # while True:
        pick_word = choice()
        a1 = jumble(pick_word)
        if a1 in ls:
            a1 = jumble(pick_word)
        else:
            print()
            print("The jumbled word is:")
            print(a1)
            print()
        print("Type 'HINT' for hint or 'PRESS ANY KEY' for guess:")
        hn = input().upper()
        if (hn == "HINT"):
            y = random.randint(0, len(pick_word)-1)
            hint.append("* "*(y))
            hint.append(pick_word[y])
            hint.append("* "*((len(pick_word)-1)-y))
            score -= 0.5

            print(*hint)
            hint = []
        else:
            pass
        a = input("Enter the word you are thinking of:\n").upper()
        # time.sleep(5)
        # print("write 'HINT' for hint!")
        if a in ls:
            score += 1
            print()
            print("Yeah! You guessed right")
            print()
        else:
            print()
            print("Better luck next time!")
            print()
            print("The correct word is")
            print(pick_word)
            print()
    print(player1, "Your score is:", score, "out of 5.")
#     print(player2,"Your score is:", score)


play()
