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

    #function for help
    # creating class for button 'HELP':
    help = Frame(w, width=800, height=600)
    help.place(anchor='center', relx=0.5, rely=0.5)
    w.title('HELP')
    # h.pack()
    # Create a Label Widget to display the text or Image
    label3 = Label(help, image=img)

    def helpToHome():
        help.pack_forget()
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