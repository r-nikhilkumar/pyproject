import tkinter as tk
from PIL import Image, ImageTk
run = tk.Tk()

def go():
    frame1.pack_forget()
    frame2.pack()



img = ImageTk.PhotoImage(Image.open('forest1.jpeg'))
frame1 = tk.Frame(run, width=400, height=400)
lab = tk.Label(frame1, image=img)
lab1t = tk.Label(frame1, text="its frame 1")
but = tk.Button(frame1, text="goto2",command=go)
lab.pack()
lab1t.pack()
but.pack()
frame1.pack()

frame2 = tk.Frame(run, width=400, height=400)
lab2 = tk.Label(frame2, image=img)
lab2.place(anchor=tk.CENTER,relx=0.5,rely=0.5)
lab2t = tk.Label(frame2, text="its frame 2")
lab2t.place(anchor=tk.CENTER,relx=0.5,rely=0.5)
lab2.pack()
lab2t.pack()









run.mainloop()