from tkinter import *
import random
def next_turn(row,column):
    global players
    if buttons[row][column]['text']=="" and winner() is False:
             if players==player[0]:
                 buttons[row][column]['text']=players
                 label.config(fg="#317773")
                 if winner() is False:
                     players=player[1]
                     label.config(text=(player[1]+" Turn"),fg="#317773")
                 elif winner() is True:
                     label.config(text=(player[0]+" Wins"),fg="#CC313D")
                 elif winner()=="Tie":
                     label.config(text=("Tie"),fg="#317773")
             else:
                 buttons[row][column]['text']=players
                 label.config(fg="#317773")
                 if winner() is False:
                     players=player[0]
                     label.config(text=(player[0]+" Turn"),fg="#317773")
                 elif winner() is True:
                    label.config(text=(player[1]+" Wins"),fg="#CC313D")
                 elif winner()=="Tie":
                    label.config(text=("Tie"),fg="red")
                 
def reset_game():
    global players
    players=random.choice(player)
    label.config(text=players+" Turn",fg="#317773")
    for row in range(3):
         for column in range(3):
                  buttons[row][column].config(text="",bg="white")
def empty():
    emptysp=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                emptysp -=1
    if emptysp==0:
        return False
    else:
        return True
            
def winner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!="":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text']!="":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty() is False:
        for row in range(3):
            for column in range(3):
               buttons[row][column].config(bg="red")
        return "Tie"
    else:
        return False
window=Tk()
window.title("Tic-Tac-Toe")
window.config(bg="#E3B448")
frame=Frame(window)
frame.pack()
buttons=[[0,0,0],[0,0,0],[0,0,0]]
player=["X","O"]
players=random.choice(player)
label=Label(text=players + " Turn",font=("Helvetica","50"),bg="#E3B448")
label.pack(side="top")
btn=Button(text="RESET" ,font=40,command=reset_game,activebackground="blueviolet",activeforeground="violet")
btn.pack(side="top")
for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text='',bg="white",font=40,height=3,
        width=5,command=lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
        label.config(fg="#317773")
window.mainloop()
