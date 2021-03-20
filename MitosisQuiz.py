"""
Script: MitosisQuiz.py
Programmer: Declan O'Brien
Date: March 4, 2021

Assignment: Final Practice Create Project

Purpose: Educate About Mitosis through a matching quiz

Function: Display images of the stages of Mitosis and
corresponding text boxes in a random order and the stage
options in a predetermined order. The user’s answers are
compared to the correct answers to determine the results and score.
"""


"""
Issues: Widgets must be added to a list
before they are placed in order for them to
be accessible from the list
"""


# import packages
from tkinter import *
import random


# create window and heading
window = Tk()
window.title("Mitosis Quiz")
window.configure(background="black")
window.state("zoomed")
header = Label(window, text="Mitosis Quiz!", fg="deep sky blue",\
               bg="black", font="ComicSansMS 40 bold")\
               .place(relx=0.5, anchor=N)
subheader = Label(window, text="Type the letter of the stage of mitosis "\
                  +"in each box corresponding to the image above.",\
                  font="ComicSansMS 18", fg="white", bg="black")\
                  .place(relx=0.5, rely=0.089, anchor=N)
"""
DevByDecLogo = PhotoImage(file="DevByDecLogo.gif")
logo = Label(window, image=DevByDecLogo).place(rely=0.5, relx=0.5, anchor=CENTER)
"""


# horizontal locations of the mitosis stages
imageLocations = [0.1, 0.26, 0.42, 0.58, 0.73, 0.89]


# place choices before list is shuffled
# so they are always in the same order
# and the images are not
choices = []
c1 = Label(window, text="A. Interphase", bg="black", fg="white", font="Helvetica 15")
choices.append(c1)
c2 = Label(window, text="B. Prophase", bg="black", fg="white", font="Helvetica 15")
choices.append(c2)
c3 = Label(window, text="C. Metaphase", bg="black", fg="white", font="Helvetica 15")
choices.append(c3)
c4 = Label(window, text="D. Anaphase", bg="black", fg="white", font="Helvetica 15")
choices.append(c4)
c5 = Label(window, text="E. Telophase", bg="black", fg="white", font="Helvetica 15")
choices.append(c5)
c6 = Label(window, text="F. Cytokinesis", bg="black", fg="white", font="Helvetica 15")
choices.append(c6)
# place choices in order
for location in imageLocations:
    choices[0].place(relx=location, rely=0.75, anchor=CENTER)
    choices.remove(choices[0])


# add all mitosis images to a list
images = []
interphase = PhotoImage(file="interphase.gif")
i = Label(window, image=interphase)
images.append(i)
prophase = PhotoImage(file="prophase.gif")
p = Label(window, image=prophase)
images.append(p)
metaphase = PhotoImage(file="metaphase.gif")
m = Label(window, image=metaphase)
images.append(m)
anaphase = PhotoImage(file="anaphase.gif")
a = Label(window, image=anaphase)
images.append(a)
telophase = PhotoImage(file="telophase.gif")
t = Label(window, image=telophase)
images.append(t)
cytokinesis = PhotoImage(file="cytokinesis.gif")
c = Label(window, image=cytokinesis)
images.append(c)
# add all answer boxes to a list
answerBoxes = []
a1 = Entry(window, borderwidth=5, font="Helvetica 15 bold", justify=CENTER, width=3)
answerBoxes.append(a1)
a2 = Entry(window, borderwidth=5, font="Helvetica 15 bold", justify=CENTER, width=3)
answerBoxes.append(a2)
a3 = Entry(window, borderwidth=5, font="Helvetica 15 bold", justify=CENTER, width=3)
answerBoxes.append(a3)
a4 = Entry(window, borderwidth=5, font="Helvetica 15 bold", justify=CENTER, width=3)
answerBoxes.append(a4)
a5 = Entry(window, borderwidth=5, font="Helvetica 15 bold", justify=CENTER, width=3)
answerBoxes.append(a5)
a6 = Entry(window, borderwidth=5, font="Helvetica 15 bold", justify=CENTER, width=3)
answerBoxes.append(a6)


# randomize Mitosis Images and their corresponding answer boxes
def randomizeMitosisImages():
    # randomize image locations
    random.shuffle(imageLocations)
    # place each mitosis stage and each corresponding
    # answer box in the next random location
    stage = 0
    while stage < len(images):
        images[stage].place(relx=imageLocations[stage], rely=0.35, anchor=CENTER)
        answerBoxes[stage].place(relx=imageLocations[stage], rely=0.5, anchor=CENTER)
        stage += 1


# call the randomizer to start the game
randomizeMitosisImages()


# create check answer function
def checkAnswer(a, b, c, d, e, f):
    # hide the check answer button
    checkAnswerButton.place_forget()
    score = 0
    global results
    results = []
    # print results
    if ("a" in a) or ("A" in a):
        correct1 = Label(window, text="Correct!", font="Helvetica 20 bold", fg="green",\
                         bg="black")
        results.append(correct1)
        correct1.place(relx=imageLocations[0], rely=0.2, anchor=CENTER)
        score += 1
    else:
        incorrect1 = Label(window, text="Incorrect", font="Helvetica 20 bold", fg="red",\
                         bg="black")
        ca1 = Label(window, text="Correct Answer:\nA. Interphase", font="Helvetica 15", fg="gray64",\
                    bg="black")
        results.extend([incorrect1, ca1])
        incorrect1.place(relx=imageLocations[0], rely=0.16, anchor=CENTER)
        ca1.place(relx=imageLocations[0], rely=0.22, anchor=CENTER)
    if ("b" in b) or ("B" in b):
        correct2 = Label(window, text="Correct!", font="Helvetica 20 bold", fg="green",\
                         bg="black")
        results.append(correct2)
        correct2.place(relx=imageLocations[1], rely=0.2, anchor=CENTER)
        score += 1
    else:
        incorrect2 = Label(window, text="Incorrect", font="Helvetica 20 bold", fg="red",\
                         bg="black")
        ca2 = Label(window, text="Correct Answer:\nB. Prophase", font="Helvetica 15", fg="gray64",\
                    bg="black")
        results.extend([incorrect2, ca2])
        incorrect2.place(relx=imageLocations[1], rely=0.16, anchor=CENTER)
        ca2.place(relx=imageLocations[1], rely=0.22, anchor=CENTER)
    if ("c" in c) or ("C" in c):
        correct3 = Label(window, text="Correct!", font="Helvetica 20 bold", fg="green",\
                         bg="black")
        results.append(correct3)
        correct3.place(relx=imageLocations[2], rely=0.2, anchor=CENTER)
        score += 1
    else:
        incorrect3 = Label(window, text="Incorrect", font="Helvetica 20 bold", fg="red",\
                         bg="black")
        ca3 = Label(window, text="Correct Answer:\nC. Metaphase", font="Helvetica 15", fg="gray64",\
                    bg="black")
        results.extend([incorrect3, ca3])
        incorrect3.place(relx=imageLocations[2], rely=0.16, anchor=CENTER)
        ca3.place(relx=imageLocations[2], rely=0.22, anchor=CENTER)
    if ("d" in d) or ("D" in d):
        correct4 = Label(window, text="Correct!", font="Helvetica 20 bold", fg="green",\
                         bg="black")
        results.append(correct4)
        correct4.place(relx=imageLocations[3], rely=0.2, anchor=CENTER)
        score += 1
    else:
        incorrect4 = Label(window, text="Incorrect", font="Helvetica 20 bold", fg="red",\
                         bg="black")
        ca4 = Label(window, text="Correct Answer:\nD. Anaphase", font="Helvetica 15", fg="gray64",\
                    bg="black")
        results.extend([incorrect4, ca4])
        incorrect4.place(relx=imageLocations[3], rely=0.16, anchor=CENTER)
        ca4.place(relx=imageLocations[3], rely=0.22, anchor=CENTER)
    if ("e" in e) or ("E" in e):
        correct5 = Label(window, text="Correct!", font="Helvetica 20 bold", fg="green",\
                         bg="black")
        results.append(correct5)
        correct5.place(relx=imageLocations[4], rely=0.2, anchor=CENTER)
        score += 1
    else:
        incorrect5 = Label(window, text="Incorrect", font="Helvetica 20 bold", fg="red",\
                         bg="black")
        ca5 = Label(window, text="Correct Answer:\nE. Telophase", font="Helvetica 15", fg="gray64",\
                    bg="black")
        results.extend([incorrect5, ca5])
        incorrect5.place(relx=imageLocations[4], rely=0.16, anchor=CENTER)
        ca5.place(relx=imageLocations[4], rely=0.22, anchor=CENTER)
    if ("f" in f) or ("F" in f):
        correct6 = Label(window, text="Correct!", font="Helvetica 20 bold", fg="green",\
                         bg="black")
        results.append(correct6)
        correct6.place(relx=imageLocations[5], rely=0.2, anchor=CENTER)
        score += 1
    else:
        incorrect6 = Label(window, text="Incorrect", font="Helvetica 20 bold", fg="red",\
                         bg="black")
        ca6 = Label(window, text="Correct Answer:\nF. Cytokinesis", font="Helvetica 15", fg="gray64",\
                    bg="black")
        results.extend([incorrect6, ca6])
        incorrect6.place(relx=imageLocations[5], rely=0.16, anchor=CENTER)
        ca6.place(relx=imageLocations[5], rely=0.22, anchor=CENTER)
    # display final score
    global finalScoreLabel
    finalScoreLabel = []
    finalScore = Label(window, text="FINAL SCORE:  " + str(score) + "  /  6",\
                       font="Helvetica 32 bold", bg="black", fg="gray64")
    finalScoreLabel.append(finalScore)
    finalScore.place(relx=0.5, rely=0.87, anchor=CENTER)
    # display reset button
    resetButton.place(relx=0.5, rely=0.63, anchor=CENTER)
    # clear and hide all the answer boxes
    answerBox = 0
    while answerBox < len(answerBoxes):
        answerBoxes[answerBox].place_forget()
        answerBoxes[answerBox].delete(0, "end")
        answerBox += 1

# create check answer button
checkAnswerButton = Button(window, text="Check Answers", font="Helvetica 18",\
                     fg="white", activeforeground="white",\
                     command=lambda: checkAnswer(a1.get(), a2.get(), a3.get(), a4.get(), a5.get(), a6.get()),\
                     bg="deep sky blue", activebackground="DeepSkyBlue3")
checkAnswerButton.place(relx=0.5, rely=0.63, anchor=CENTER)


# create reset function
def reset():
    # hide the reset button
    resetButton.place_forget()
    # hide all the results
    result = 0
    while result < len(results):
        results[result].place_forget()
        result += 1
    # hide the final score
    finalScoreLabel[0].place_forget()
    # hide all the mitosis images
    image = 0
    while image < len(images):
        images[image].place_forget()
        image += 1
    # rerandomize and replace all the images
    # and answer boxes
    randomizeMitosisImages()
    # replace check answer button
    checkAnswerButton.place(relx=0.5, rely=0.63, anchor=CENTER)

# create reset button
resetButton = Button(window, text="RESET", font="Helvetica 18",\
                     fg="white", activeforeground="white",\
                     bg="purple", activebackground="purple4",\
                     command=reset)


# run the window
window.mainloop()