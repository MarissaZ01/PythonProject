from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

window=Tk()
window.title("Hangman")

word_list = ["PARI ", "SINGA ", " PANDA", " BURUNG", "KUCING ", " TIKUS", "KUDA ", " TUPAI"]

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

def newGame():
    messagebox.showinfo("Petunjuk", "Tebak nama Hewan")
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces="".join(the_word)
    print(the_word_withSpaces)
    the_word_withSpaces="".join(the_word_withSpaces.split())
    print(the_word_withSpaces)
    lblWord.set(" ".join("_"*len(the_word)))

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<11:
        txt=list(the_word_withSpaces)
        print(txt)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hasil", "Anda Menang")
                    newGame()
        else:
                numberOfGuesses+=1
                imgLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses==11:
                 messagebox.showwarning("Hasil", "Kalah...")
    
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Calibri 30 bold")).grid(row=0, column=2, columnspan=4, padx=10)
n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("TimesNewRoman 20"), width=5).grid(row=1+n//9, column=n%9)
    n+=1

Button(window, text="new\nGame", command=lambda:newGame(),font=("TimesNewRoman 15 bold")).grid(row=0, column=8, sticky="NSWE")

newGame()    
window.mainloop()