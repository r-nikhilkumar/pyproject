#Packages imported
from tkinter import *
from PIL import ImageTk, Image



# initializing window:
w = Tk()

screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
a=str(screen_width)+'x'+str(screen_height)
w.geometry(a)
w.maxsize(screen_width,screen_height)
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

    aboutBack= Button(help, text="BACK", font="Helvetica,32", command=helpToHome)
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

    aboutBack= Button(about, text="BACK", font="Helvetica,32", command=aboutToHome)
    aboutBack.place(relx=0.5, rely=0.8, anchor=CENTER)
    label3.pack()

    def homeToAbout():
        home.pack_forget()
        ab.about.pack()


class st:
    start = Frame(w, width=800, height=600)
    start.place(anchor='center', relx=0.5, rely=0.5)
    w.title('START')

    # Create a Label Widget to display the text or Image
    label4 = Label(start, image=img)

    def startToHome():
        st.start.pack_forget()
        home.pack()

    startBack = Button(start, text="BACK", font="Helvetica,32", command=startToHome)
    startBack.place(relx=0.5, rely=0.8, anchor=CENTER)
    label4.pack()

    def homeToStart():
        home.pack_forget()
        st.start.pack()

# defining frame 1:


home = Frame(w, width=800, height=600)
home.place(anchor='center', relx=0.5, rely=0.5)
w.title('Jumblee')
# Create a Label Widget to display the text or Image
label = Label(home, image=img)
label.pack()
aboutBut = Button(home, text="ABOUT", font="Helvetica,32",command=ab.homeToAbout)
helpBut = Button(home, text="HELP", font="Helvetica,32", command=hel.homeToHelp)
aboutBut.place(relx=0.5, rely=0.6, anchor=CENTER)
helpBut.place(relx=0.5, rely=0.7, anchor=CENTER)
startBut = Button(home, text="START!!", font="Helvetica,32",command=st.homeToStart)
startBut.place(relx=0.5, rely=0.5, anchor=CENTER)

home.pack()
w.mainloop()
