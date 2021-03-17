"""
Script: DerivativeMemoryGame.py
Programmer: Declan O'Brien
Date: February 1, 2021

Assignment: Kickstarter Program

Purpose: To test the user's knowledge of common derivatives with a fun memory game.

Function: Use tkinter to create a GUI with cards that are flipped by the user.
"""



"""
Issues:
destroying the matched pair caused an error because the\
flip function still contained the destroyed widgets,\
so I forgot them instead

I needed to make the variable count global in order\
to get it to add within the remove function

"""

# import tkinter
from tkinter import *
# import threading
import threading


# intialize window
window = Tk()
# set title
window.title("Derivative Memory Game")
# set background color
window.configure(background="deep sky blue")
# sets the window to fullscreen
window.state("zoomed")


# heading
header = Label(window, text="Welcome to the Derivative Memory Game!",\
               bg="white", fg="black", font="ComicSansMS 40 bold")
header.place(relx=0.5, anchor=N)
subheader = Label(window, text="Test your knowledge of derivatives, as well as your memory.",\
                  bg="white", fg="gray", font="ComicSansMS 18")
subheader.place(relx=0.5, rely=0.089, anchor=N)

# instructions
i1 = Label(window, text="Instructions: Match each function to its derivative.",\
           bg="deep sky blue", fg="gray35", font="CourierNew 16")
i1.place(relx=0.5, rely=0.23, anchor=CENTER)
i2 = Label(window, text="Click a card to flip it.",\
           bg="deep sky blue", fg="gray35", font="CourierNew 16")
i2.place(relx=0.5, rely=0.27, anchor=CENTER)


"""
WHAT HAPPENS AFTER A CARD IS CLICKED
"""


# used these lists to determine which cards have been flipped
# the first list contains the text on the front of the cards to determine if they are a match
cardList1 = []
# if the cards are not a match, this list replaces the backs of the cards corresponding to the numbers
cardList2 = []


# create the result labels
match = Label(window, text="Match!", bg="deep sky blue", fg="green", font="Georgia 35 bold")
notMatch = result2 = Label(window, text="Try Again", bg="deep sky blue", fg="red", font="Georgia 35 bold")


# game over label
gameOver = Label(window, text="GAME OVER", bg="deep sky blue", fg="black", font="TimesNewRoman 50 bold")
# add 1 to count every time a match is made
count = 0


# flip whichever card is clicked, and add to the lists
def flip(num):
    # forget the instructions at the start for the rest of the game
    i1.place_forget()
    i2.place_forget()
    # add the number of the card to the second list
    cardList2.append(num)
    if num == 1:
        # do the following for each card
        # hide the back of the card
        card1.place_forget()
        # add the text to the first list
        cardList1.append(sinx["text"])
    elif num == 2:
        card2.place_forget()
        cardList1.append(ex["text"])
    elif num == 3:
        card3.place_forget()
        cardList1.append(threeXSquared["text"])
    elif num == 4:
        card4.place_forget()
        cardList1.append(sixX["text"])
    elif num == 5:
        card5.place_forget()
        cardList1.append(secantSquaredX["text"])
    elif num == 6:
        card6.place_forget()
        cardList1.append(ex2["text"])
    elif num == 7:
        card7.place_forget()
        cardList1.append(oneOverX["text"])
    elif num == 8:
        card8.place_forget()
        cardList1.append(cosx["text"])
    elif num == 9:
        card9.place_forget()
        cardList1.append(tanx["text"])
    elif num == 10:
        card10.place_forget()
        cardList1.append(lnx["text"])
    # used the texts on the front of the cards
    # to determine if the two flipped cards match
    # used threading to allow multiple functions to run at the same time in case it lags
    if (len(cardList2)) == 2:
        # disable all cards that are not part of the pair
        for x in allCards:
            if x not in cardList2:
                x["state"] = "disabled"
        if (sinx["text"] in cardList1) and (cosx["text"] in cardList1):
            # if the correct cards are in the list together and
            # therefore match, show the result
            match.place(relx=0.5, rely=0.25, anchor=CENTER)
            # forget the cards as well as the result after 2 seconds
            card1.after(2000, threading.Thread(target=lambda: remove(1)).start)
        elif (ex["text"] in cardList1) and (ex2["text"] in cardList1):
            match.place(relx=0.5, rely=0.25, anchor=CENTER)
            card2.after(2000, threading.Thread(target=lambda: remove(2)).start)
        elif (threeXSquared["text"] in cardList1) and (sixX["text"] in cardList1):
            match.place(relx=0.5, rely=0.25, anchor=CENTER)
            card3.after(2000, threading.Thread(target=lambda: remove(3)).start)
        elif (secantSquaredX["text"] in cardList1) and (tanx["text"] in cardList1):
            match.place(relx=0.5, rely=0.25, anchor=CENTER)
            card5.after(2000, threading.Thread(target=lambda: remove(4)).start)
        elif (oneOverX["text"] in cardList1) and (lnx["text"] in cardList1):
            match.place(relx=0.5, rely=0.25, anchor=CENTER)
            card7.after(2000, threading.Thread(target=lambda: remove(5)).start)
        # if two cards have been flipped and they are not a match,
        # show the result and replace the backs of the cards that are in cardList2
        else:
            notMatch.place(relx=0.5, rely=0.25, anchor=CENTER)
            window.after(2000, flipBack)
   

# if the correct cards are in the list together and
# therefore match, forget the cards and the result
def remove(num2):
    match.place_forget()
    if num2 == 1:
        # forget both the front and back of each card of the matched pair
        card1.place_forget()
        sinx.place_forget()
        card8.place_forget()
        cosx.place_forget()
    elif num2 == 2:
        card2.place_forget()
        ex.place_forget()
        card6.place_forget()
        ex2.place_forget()
    elif num2 == 3:
        card3.place_forget()
        threeXSquared.place_forget()
        card4.place_forget()
        sixX.place_forget()
    elif num2 == 4:
        card5.place_forget()
        secantSquaredX.place_forget()
        card9.place_forget()
        tanx.place_forget()
    elif num2 == 5:
        card7.place_forget()
        oneOverX.place_forget()
        card10.place_forget()
        lnx.place_forget()
    # add 1 to the global variable count
    global count
    count += 1
    # when all matches have been made, show game over
    if count == 5:
        gameOver.place(relx=0.5, rely=0.5, anchor=CENTER)
    # reenable the rest of the cards
    for x in allCards:
        if x not in cardList2:
            x["state"] = "normal"
    # clear both lists so they reset
    cardList1.clear()
    cardList2.clear()
   

# if two cards have been flipped and they are not a match,
# forget the result and replace the backs of the cards that are in cardList2
def flipBack():
    notMatch.place_forget()
    if 1 in cardList2:
        card1.place(relx=0.1, rely=0.45, anchor=CENTER)
    if 2 in cardList2:
        card2.place(relx=0.3, rely=0.45, anchor=CENTER)
    if 3 in cardList2:
        card3.place(relx=0.5, rely=0.45, anchor=CENTER)
    if 4 in cardList2:
        card4.place(relx=0.7, rely=0.45, anchor=CENTER)
    if 5 in cardList2:
        card5.place(relx=0.9, rely=0.45, anchor=CENTER)
    if 6 in cardList2:
        card6.place(relx=0.1, rely=0.75, anchor=CENTER)
    if 7 in cardList2:
        card7.place(relx=0.3, rely=0.75, anchor=CENTER)
    if 8 in cardList2:
        card8.place(relx=0.5, rely=0.75, anchor=CENTER)
    if 9 in cardList2:
        card9.place(relx=0.7, rely=0.75, anchor=CENTER)
    if 10 in cardList2:
        card10.place(relx=0.9, rely=0.75, anchor=CENTER)
    # reenable the rest of the cards
    for x in allCards:
        if x not in cardList2:
            x["state"] = "normal"
    # clear both lists so they reset
    cardList1.clear()
    cardList2.clear()



"""
CREATING THE CARDS
"""

# card image
card = PhotoImage(file="card.gif")

# list of all cards
allCards = []

# for each card, the front with the equation is put on the screen, and then the back
# used lambda to allow the button click to have parameters

# first row of cards
sinx = Label(window, text="f(x)=sin(x)", fg="red", font="ComicSansMS 16", bg="black", width=8, height=6)
sinx.place(relx=0.1, rely=0.45, anchor=CENTER)
card1 = Button(window, image=card, bg="black", command=lambda: flip(1))
card1.place(relx=0.1, rely=0.45, anchor=CENTER)
allCards.append(card1)

ex = Label(window, text="f'(x)=e^x", fg="red", font="ComicSansMS 16", bg="black", width=8, height=6)
ex.place(relx=0.3, rely=0.45, anchor=CENTER)
card2 = Button(window, image=card, bg="black", command=lambda: flip(2))
card2.place(relx=0.3, rely=0.45, anchor=CENTER)
allCards.append(card2)

threeXSquared = Label(window, text="f(x)=3x^2", fg="red", font="ComicSansMS 16", bg="black", width=8, height=6)
threeXSquared.place(relx=0.5, rely=0.45, anchor=CENTER)
card3 = Button(window, image=card, bg="black", command=lambda: flip(3))
card3.place(relx=0.5, rely=0.45, anchor=CENTER)
allCards.append(card3)

sixX = Label(window, text="f'(x)=6x", fg="red", font="ComicSansMS 16", bg="black", width=8, height=6)
sixX.place(relx=0.7, rely=0.45, anchor=CENTER)
card4 = Button(window, image=card, bg="black", command=lambda: flip(4))
card4.place(relx=0.7, rely=0.45, anchor=CENTER)
allCards.append(card4)

secantSquaredX = Label(window, text="f'(x)=sec^2(x)", fg="red", font="ComicSansMS 12", bg="black", width=11, height=8)
secantSquaredX.place(relx=0.9, rely=0.45, anchor=CENTER)
card5 = Button(window, image=card, bg="black", command=lambda: flip(5))
card5.place(relx=0.9, rely=0.45, anchor=CENTER)
allCards.append(card5)

# second row of cards
ex2 = Label(window, text="f(x)=e^x", fg="red", font="ComicSansMS 16", bg="black", width=8, height=6)
ex2.place(relx=0.1, rely=0.75, anchor=CENTER)
card6 = Button(window, image=card, bg="black", command=lambda: flip(6))
card6.place(relx=0.1, rely=0.75, anchor=CENTER)
allCards.append(card6)

oneOverX = Label(window, text="f'(x)=1/x", fg="red", font="ComicSansMS 16", bg="black", width=8, height=6)
oneOverX.place(relx=0.3, rely=0.75, anchor=CENTER)
card7 = Button(window, image=card, bg="black", command=lambda: flip(7))
card7.place(relx=0.3, rely=0.75, anchor=CENTER)
allCards.append(card7)

cosx = Label(window, text="f'(x)=cos(x)", fg="red", font="ComicSansMS 16", bg="black", width=8, height=6)
cosx.place(relx=0.5, rely=0.75, anchor=CENTER)
card8 = Button(window, image=card, bg="black", command=lambda: flip(8))
card8.place(relx=0.5, rely=0.75, anchor=CENTER)
allCards.append(card8)

tanx = Label(window, text="f(x)=tan(x)", fg="red", font="ComicSansMS 16", bg="black", width=8, height=6)
tanx.place(relx=0.7, rely=0.75, anchor=CENTER)
card9 = Button(window, image=card, bg="black", command=lambda: flip(9))
card9.place(relx=0.7, rely=0.75, anchor=CENTER)
allCards.append(card9)

lnx = Label(window, text="f(x)=ln(x)", fg="red", font="ComicSansMS 16", bg="black", width=8, height=6)
lnx.place(relx=0.9, rely=0.75, anchor=CENTER)
card10 = Button(window, image=card, bg="black", command=lambda: flip(10))
card10.place(relx=0.9, rely=0.75, anchor=CENTER)
allCards.append(card10)



# run the window
window.mainloop()


