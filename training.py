# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 01:52:41 2020

@author: Yuri Borrmann
"""

import numpy as np
import pickle
import time
import random
from tqdm import tqdm

# Defining numbers of each player and board size
size = 3
player1 = 1
player2 = 2

# Rewards
win = 1
lose = -1
draw = -0.1

# How many games
epochs = 10000000

# Some parameters
epsilon = 0.3
learning_rate = 0.001
epsilon_decay = 1

# If you are going to training from scratch, it's None
start_q_table = None

if start_q_table is None:
    qtable1 = dict()
    qtable2 = dict()
    for x1 in range(3):
        for x2 in range(3):
            for x3 in range(3):
                for x4 in range(3):
                    for x5 in range(3):
                        for x6 in range(3):
                            for x7 in range(3):
                                for x8 in range(3):
                                    for x9 in range(3):
                                        qtable1[(x1,x2,x3,x4,x5,x6,x7,x8,x9)] = [np.random.normal(0,1) for i in range(9)]
                                        qtable2[(x1,x2,x3,x4,x5,x6,x7,x8,x9)] = [np.random.normal(0,1) for i in range(9)]
else:
    with open("qtable2-1582159791.pickle", "rb") as f:
        qtable2 = pickle.load(f)
    with open("qtable1-1582159791.pickle", "rb") as f:
        qtable1 = pickle.load(f)

# Player 1 playing
def play1(game, random_action):
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
    actions = qtable1[game]
    q = -10000000
    # If necessary, choose a random action
    if random_action == True:
        action = random.choice(available_place)
        q = actions[action]
    # Else, choose the best action
    else:
        for x in available_place:
            if actions[x] > q:
                q = actions[x]
                action = x
    return action, q

# Player 2 playing
def play2(game, random_action):
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
    actions = qtable2[game]
    q = -10000000
    # If necessary, choose a random action
    if random_action == True:
        action = random.choice(available_place)
        q = actions[action]
    # Else, choose the best action
    else:
        for x in available_place:
            if actions[x] > q:
                q = actions[x]
                action = x
    return action, q

# Rules of the game
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

# Games!
for epoch in tqdm(range(epochs)):
    # Starting game
    game = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    x = 0
    # Who starts?
    y = np.random.randint(0,2)
    result = 'next'
    gameold = dict()
    q1 = dict()
    q2 = dict()
    action1 = dict()
    action2 = dict()
    reward1 = 0
    reward2 = 0
    
    
    while (x < 10 and result == 'next'):
        game = np.asarray(game)
        game = np.ndarray.tolist(game)
        # Saving each game so we can update our q table
        gameold[x] = game
        game = tuple(game)
        # Player 1
        if y == 0:
            game = tuple(game)
            # 30% of plays will be random
            if np.random.random() > epsilon:
                random_action = False
            else:
                random_action = True
            # What should player 1 do?
            action, q = play1(game, random_action)
            game = np.asarray(game)
            game = np.ndarray.tolist(game)
            # Updating board
            game[action] = player1
            # Checking if game is over
            result = rules(game, player1)
            # Saving q value and action to update the q table later
            q1[x] = q
            action1[x] = action
            # Rewards
            if result == 'win':
                reward1 = win
                reward2 = lose
                result += '1'
            elif result == 'draw':
                reward1 = draw
                reward2 = draw
            # Now it's player 2 round
            y = 1
            x += 1
        # Player 2 is the same thing
        else:
            game = tuple(game)
            
            if np.random.random() > epsilon:
            # GET THE ACTION
                random_action = False
            else:
                random_action = True
            
            action, q = play2(game, random_action)
            game = np.asarray(game)
            game = np.ndarray.tolist(game)
            game[action] = player2
            result = rules(game, player2)
            q2[x] = q
            action2[x] = action
            if result == 'win':
                reward2 = win
                reward1 = lose
                result += '2'
            elif result == 'draw':
                reward2 = draw
                reward1 = draw
            y = 0
            x += 1
    # Updating q table
    for i in q2.keys():
        qtable2[tuple(gameold[i])][action2[i]] += learning_rate*reward2
    for i in q1.keys():
        qtable1[tuple(gameold[i])][action1[i]] += learning_rate*reward1
        
    epsilon += epsilon_decay

# Saving q table
with open(f"qtable1-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(qtable1, f)

with open(f"qtable2-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(qtable2, f)                