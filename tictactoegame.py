# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:17:57 2020

@author: Yuri Borrmann
"""

import numpy as np
import pickle
import tkinter
from tkinter import Tk, Button
import tkinter.messagebox

# Number of each player
player = 1
pc = 2

# Loading q table        
start_q_table = "q_table.pickle"

with open(start_q_table, "rb") as f:
    q_table = pickle.load(f)
    

# Pc playing
def playpc(game):
    available_place = list()
    i = 0
    gm = np.asarray(game)
    gm = np.ndarray.tolist(gm)
    # Check which places are available
    for x in gm:
        if x == 0:
            available_place.append(i)
        i += 1
    # All actions
    actions = q_table[game]
    q = -10000000000000000000000
    # Inside the available places, get the one with highest score
    for x in available_place:
        if actions[x] > q:
            q = actions[x]
            action = x
    return action

# Checking if the game is over
def rules(game, player):
    for x in range(0,7,3):
        if game[x] == player and (game[x + 1]) == player and (game[x + 2]) == player:
            return 'win'
    for x in range(3):
        if game[x] == player and (game[x + 3]) == player and (game[x + 6]) == player:
            return 'win'
    if game[4] == player:
        if (game[0] == player and game[8] == player) or (game[6] == player and game[2] == player):
            return 'win'
    if 0 not in game:
        return 'draw'
    
    return 'next'

# When we press a button:
def choices(button):
    global houses
    # If the chosen place is empty
    if button["text"] == " ":
        button["text"] = "X"
        # Recreating the board in a list format, so that we can pass it to the pc
        game = list()
        for x in houses:
            if x["text"] == " ":
               game.append(0)
            elif x["text"] == "X":
                game.append(player) # Player
            else:
                game.append(pc) # Pc
        # Checking if game is over
        result = rules(game, player)
        if result == 'win':
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "You won!")
            return
        elif result == 'draw':
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            return
        # Pc playing
        game = tuple(game)
        action = playpc(game)
        game = np.asarray(game)
        game = np.ndarray.tolist(game)
        game[action] = pc
        houses[action]["text"] = "O"
        game = tuple(game)
        # Checking if game is over
        result = rules(game, pc)
        if result == 'win':
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "You lost!")
            return
        elif result == 'tie':
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            return
        
        return
    else:
        return tkinter.messagebox.showinfo("Tic-Tac-Toe", "Pick again")
    
    return

x = 0
# Random variable to see who starts the game
y = np.random.randint(1,3)
# Initial game
game = (0, 0, 0, 0, 0, 0, 0, 0, 0)
result = 'next'
# If pc plays it first
if y == pc:
    game = tuple(game)
    action = playpc(game)
    game = np.asarray(game)
    game = np.ndarray.tolist(game)
    game[action] = pc
    game = tuple(game)

#Creating visual content
tk = Tk()
places = np.asarray(game)
places = np.ndarray.tolist(places)
available_places = []
board = []
houses = []
i = 0
for x in places:
    if x == 0:
        available_places.append(i)
    i += 1
for x in places:
    if x == 0:
        board.append(" ")
    elif x == 1:
        board.append("X") # Player
    else:
        board.append("O") # Pc

# Buttons
houses.append(Button(tk, text=board[0], font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: choices(houses[0])))
houses.append(Button(tk, text=board[1], font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: choices(houses[1])))
houses.append(Button(tk, text=board[2], font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: choices(houses[2])))
houses.append(Button(tk, text=board[3], font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: choices(houses[3])))
houses.append(Button(tk, text=board[4], font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: choices(houses[4])))
houses.append(Button(tk, text=board[5], font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: choices(houses[5])))
houses.append(Button(tk, text=board[6], font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: choices(houses[6])))
houses.append(Button(tk, text=board[7], font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: choices(houses[7])))
houses.append(Button(tk, text=board[8], font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: choices(houses[8])))
houses[0].grid(row=0, column=0)
houses[1].grid(row=0, column=1)
houses[2].grid(row=0, column=2)
houses[3].grid(row=1, column=0)
houses[4].grid(row=1, column=1)
houses[5].grid(row=1, column=2)
houses[6].grid(row=2, column=0)
houses[7].grid(row=2, column=1)
houses[8].grid(row=2, column=2)

# Updating if the pc was the first to play
if y == pc:
    houses[action]["text"] = "O"

# The game starts!
tk.mainloop()
