import sys
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
window = tk.Tk()
window.title("Happy Valentine's Day Babe!")
window.resizable(False, False)

def galleryopen():
    window1= Toplevel(window)
    img1=PhotoImage(file="photo1.png")
    photo1= tk.Label(window1, image=img1, background="#e5aee8")

    img2=PhotoImage(file="photo2.png")
    photo2= tk.Label(window1, image=img2, background="#e5aee8")

    img3=PhotoImage(file="photo3.png")
    photo3= tk.Label(window1, image=img3, background="#e5aee8")

    img4=PhotoImage(file="photo4.png")
    photo4= tk.Label(window1, image=img4, background="#e5aee8")

    photo1.grid(row=0, column=0, sticky=("NW"+"SE"))
    photo2.grid(row=1, column=1, sticky=("NW"+"SE"))
    photo3.grid(row=0, column=1, sticky=("NW"+"SE"))
    photo4.grid(row=1, column=0, sticky=("NW"+"SE"))
    window1.mainloop()


gallery = tk.Button(window, 
                    text="Gallery", 
                    background="#e5aee8",
                    command= galleryopen)
def noteopen():
    window3= Toplevel(window)
    window3.geometry("470x250")
    textbox = tk.Label(window3, background="#ebc3d9", text="To my Valentine <3\n \n.Since we've met I've been the happiest I could ever be,\n I cherish every second with you and hope to spend forever by your side.\n I often wish you could see what I see, that you're an amazing friend,\n a good person and the best boyfriend I could ever ask for.\n I've never met someone like you before, with so much care, thoughtfulness \n and love. I think about how we met and how unlikely it was for us to ever\n cross paths and yet we met and sometimes I think was it meant to be,\n our relationship is something I only thought I could ever dream of.\n I'm so in love with you, when you're with me I'm the happiest I can be \n (even when being woken up), and when you're gone I miss you \n and I think of you all the time. I love you so much and I wish to spend \n the rest of my life with you, getting to experience all things big and small next to you \n Happy Valentine's Day babe <3 ")
    textbox.grid(row=0,column=0)
    
 
    
    window3.mainloop()


note =tk.Button(window, 
                 text="Note", 
                 background="#e5aee8",
                 command=noteopen)

def wishopen():
    window2= Toplevel(window)
    img5=PhotoImage(file="photo5.png")
    photo5= tk.Label(window2, image=img5, background="#e5aee8")

    img6=PhotoImage(file="photo6.png")
    photo6= tk.Label(window2, image=img5, background="#e5aee8")

    img7=PhotoImage(file="photo7.png")
    photo7= tk.Label(window2, image=img7, background="#e5aee8")

    img8=PhotoImage(file="photo8.png")
    photo8= tk.Label(window2, image=img8, background="#e5aee8")

    photo5.grid(row=0, column=0, sticky=("NW"+"SE"))
    photo6.grid(row=1, column=1, sticky=("NW"+"SE"))
    photo7.grid(row=0, column=1, sticky=("NW"+"SE"))
    photo8.grid(row=1, column=0, sticky=("NW"+"SE"))
    window2.mainloop()

wish = tk.Button(window, 
                 text="Wishboard", 
                 background="#e5aee8",
                 command = wishopen)

img=PhotoImage(file="heart.png")
heart= tk.Label(window, image=img)
gallery.grid(row=0, column=0, sticky=("NW"+"SE"))
note.grid(row=0, column=1, sticky=("NW"+"SE"))
wish.grid(row=0, column=2, sticky=("NW"+"SE"))
heart.grid(row=3, column=0, pady=2, padx=2, columnspan=3)


window.mainloop() 
