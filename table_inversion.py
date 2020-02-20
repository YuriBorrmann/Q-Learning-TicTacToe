# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:21:49 2020

@author: Yuri Borrmann
"""
import pickle


with open('qtable.pickle', "rb") as f:
    q_table2 = pickle.load(f)

print(q_table2[(0,0,0,0,0,0,0,0,0)])
start_q_table = None

if start_q_table is None:
    qtable1 = dict()
#    qtable2 = dict()
    y1,y2,y3,y4,y5,y6,y7,y8,y9 = 0,0,0,0,0,0,0,0,0
    for x1 in range(3):
        for x2 in range(3):
            for x3 in range(3):
                for x4 in range(3):
                    for x5 in range(3):
                        for x6 in range(3):
                            for x7 in range(3):
                                for x8 in range(3):
                                    for x9 in range(3):
                                        if x1 == 2:
                                           y1 = 1
                                        elif x1 == 1:
                                            y1 = 2
                                        else:
                                            y1 = 0
                                            
                                        if x2 == 2:
                                           y2 = 1
                                        elif x2 == 1:
                                            y2 = 2
                                        else:
                                            y2 = 0
                                        
                                        if x3 == 2:
                                           y3 = 1
                                        elif x3 == 1:
                                            y3 = 2
                                        else:
                                            y3 = 0
                                            
                                        if x4 == 2:
                                           y4 = 1
                                        elif x4 == 1:
                                            y4 = 2
                                        else:
                                            y4 = 0
                                        
                                        if x5 == 2:
                                           y5 = 1
                                        elif x5 == 1:
                                            y5 = 2
                                        else:
                                            y5 = 0
                                            
                                        if x6 == 2:
                                           y6 = 1
                                        elif x6 == 1:
                                            y6 = 2
                                        else:
                                            y6 = 0
                                        
                                        if x7 == 2:
                                           y7 = 1
                                        elif x7 == 1:
                                            y7 = 2
                                        else:
                                            y7 = 0
                                            
                                        if x8 == 2:
                                           y8 = 1
                                        elif x8 == 1:
                                            y8 = 2
                                        else:
                                            y8 = 0
                                        
                                        if x9 == 2:
                                           y9 = 1
                                        elif x9 == 1:
                                            y9 = 2
                                        else:
                                            y9 = 0
                                            
                                        qtable1[(y1,y2,y3,y4,y5,y6,y7,y8,y9)] = q_table2[(x1,x2,x3,x4,x5,x6,x7,x8,x9)]
                                        

with open(f"qtable2-100milhoes-invertida.pickle", "wb") as f:
    pickle.dump(qtable1, f)