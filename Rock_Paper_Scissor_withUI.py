from random import randint
from tkinter import *
from PIL import Image, ImageTk

#Home window
root = Tk()
root.title("Rock Paper Scissor!")
root.configure(background="azure2")

#Title
title = Label(root, font=100, text="!!Stone Paper Scissors!!", bg="azure2", fg="Black").grid(row = 0, column=2)

#User pictures
R_image = ImageTk.PhotoImage(Image.open("rock.png"))
P_image = ImageTk.PhotoImage(Image.open("paper.png"))
S_image = ImageTk.PhotoImage(Image.open("scissor.png"))

#Comp pictures
RC_image = ImageTk.PhotoImage(Image.open("rock_comp.png"))
PC_image = ImageTk.PhotoImage(Image.open("paper_comp.png"))
SC_image = ImageTk.PhotoImage(Image.open("scissor_comp.png"))

#insert picture
user_label = Label(root,image=R_image)
user_label.grid(row=1, column=4)

comp_label = Label(root ,image=RC_image)
comp_label.grid(row=1, column=0)

#scores
user_scores = Label(root,text=0, font=100, bg="azure2", fg="Black")
user_scores.grid(row=1, column=3)

comp_scores = Label(root,text=0, font=100, bg="azure2", fg="Black")
comp_scores.grid(row=1, column=1)

#indicator
user_indicator = Label(root, font=50, text="USER", bg="azure2", fg="Black").grid(row = 2, column=3)
comp_indicator = Label(root, font=50, text="COMPUTER", bg="azure2", fg="Black").grid(row=2, column=1)

#Message
msg = Label(root, font=50, bg="azure2", fg="Black")
msg.grid(row = 3, column=2)

#update messages
def updateMsg(x):
    msg['text'] = x

#update comp score
def update_comp_score():
    score = int(comp_scores["text"])
    score+=1
    comp_scores["text"] = str(score)

#update user score
def update_user_score():
    score = int(user_scores["text"])
    score+=1
    user_scores["text"] = str(score)

#check winner
def winner(user, comp):
    if user == comp:
        updateMsg("Tie!!")

    elif user == "rock":
        if comp == "paper":
            updateMsg("You Lose")
            update_comp_score()
        else:
            updateMsg("You Win")
            update_user_score()
    elif user == "paper":
        if comp == "scissor":
            updateMsg("You Lose")
            update_comp_score()
        else:
            updateMsg("You Win")
            update_user_score()
    elif user == "scissor":
        if comp == "rock":
            updateMsg("You Lose")
            update_comp_score()
        else:
            updateMsg("You Win")
            update_user_score()
    else:
        pass


#update Choices
choices = ["rock", "paper", "scissor"]



def up_choices(x):
#for computer
    comp_choice = choices[randint(0,2)]
    if comp_choice == "rock":
        comp_label.configure(image=RC_image)
    elif comp_choice == "paper":
        comp_label.configure(image=PC_image)
    else:
        comp_label.configure(image=SC_image)
    
#for user
    if x == "rock":
        user_label.configure(image=R_image)
    elif x == "paper":
        user_label.configure(image=P_image)
    else:
        user_label.configure(image=S_image)
        
    winner(x,comp_choice)

#button
button1 = Button(root, width=20, height=2, text="Rock",
            bg="deep sky blue", fg="Black",
             command = lambda:up_choices("rock")).grid(row=4,column=1)


button2 = Button(root, width=20, height=2, text="Paper",
            bg="deep sky blue", fg="Black",
             command = lambda:up_choices("paper")).grid(row=4,column=2)


button3 = Button(root, width=20, height=2, 
            text="Scissor",bg="deep sky blue", fg="Black", 
            command = lambda:up_choices("scissor")).grid(row=4,column=3)


root.mainloop()
