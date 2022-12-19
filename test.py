import tkinter as tk
from PIL import Image, ImageTk
run = tk.Tk()

# def go():
#     frame1.pack_forget()
#     frame2.pack()

# # while run:
#     #     while True:
#     #         x = random.randint(0, len(w)-1)
#     #         if x not in ls:
#     #             ls.append(x)
#     #         if len(ls) == len(w):
#     #             break

#     #     word = ""
#     #     for i in ls:
#     #         word += w[i]+" "
#     #     if word != w:
#     #         run = False
#     # # print(ls)


# img = ImageTk.PhotoImage(Image.open('forest1.jpeg'))
frame1 = tk.Frame(run, width=400, height=400)
# lab = tk.Label(frame1, image=img)
# lab.place(anchor=tk.CENTER, relx=0.5,rely=0.5)
# lab1t = tk.Label(frame1, text="its frame 1")
# lab1t.place(anchor=tk.CENTER,relx=0.5,rely=0.6)
# but = tk.Button(frame1, text="goto2",command=go)
# but.place(relx=0.5,rely=0.7,anchor=tk.CENTER)

# lab.pack()
# lab1t.pack()
# but.pack()
# frame2 = tk.Frame(run, width=400, height=400)
# lab2 = tk.Label(frame2, image=img)
# lab2.place(anchor=tk.CENTER,relx=0.5,rely=0.5)
# lab2t = tk.Label(frame2, text="its frame 2")
# lab2t.place(anchor=tk.CENTER,relx=0.5,rely=0.5)
# lab2.pack()
# lab2t.pack()

def set():
    lebel.configure(text=clicked.get())
clicked = tk.StringVar()
level = tk.OptionMenu(frame1,clicked,'EASY','MEDIUM','HARD',command=set)
level = tk.OptionMenu()
# clicked = level.getvar()
lebel = tk.Label(frame1, text=clicked.get())
level.pack()
lebel.pack()
frame1.pack()









run.mainloop()