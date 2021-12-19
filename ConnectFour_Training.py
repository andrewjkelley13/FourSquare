import numpy as np
import matplotlib.pyplot as pt
import torch as tr
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def state_string(state):
    return "\n".join(["".join(row) for row in state])

def det_player_type():
    player1_type = input("Player 1: Enter 0 for human control, Enter 1 for baseline AI, Enter 2 for Tree-Based:\n")
    player2_type = input("Player 2: Enter 0 for human control, Enter 1 for baseline AI, Enter 2 for Tree-Based:\n")
    return player1_type,player2_type

def det_board_size():
    boardsize = input("To train NN, Enter 0 for a 5x6 board, Enter 1 for a 7x6 board, Enter 2 for a 9x6 board, Enter 3 for a 3x6 board:\n")
    return boardsize

def score(state,boardsize):
    if boardsize == "0":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
        vert3 = state[4,3],state[3,3],state[2,3],state[1,3],state[0,3]
        vert4 = state[5,4],state[4,4],state[3,4],state[2,4],state[1,4],state[0,4]
        horiz0 = state[0,4],state[0,3],state[0,2],state[0,1],state[0,0]
        horiz1 = state[1,4],state[1,3],state[1,2],state[1,1],state[1,0]
        horiz2 = state[2,4],state[2,3],state[2,2],state[2,1],state[2,0]
        horiz3 = state[3,4],state[3,3],state[3,2],state[3,1],state[3,0]
        horiz4 = state[4,4],state[4,3],state[4,2],state[4,1],state[4,0]
        diag0 = state[5,0],state[4,1],state[3,2],state[2,3],state[1,4]
        diag1 = state[4,0],state[3,1],state[2,2],state[1,3],state[0,4]
        diag2 = state[3,0],state[2,1],state[1,2],state[0,3]
        diagback0 = state[3,4],state[2,3],state[1,2],state[0,1]
        diagback1 = state[4,4],state[3,3],state[2,2],state[1,1],state[0,0]
        diagback2 = state[5,4],state[4,3],state[3,2],state[2,1],state[1,0]
    
    
        for player,value in (("X",1),("O",-1)):
            for h0 in range(len(horiz0)):
                if h0 < 2:
                    if (horiz0[h0] == horiz0[h0+1] == horiz0[h0+2] == horiz0[h0+3] == player): return value
            for h1 in range(len(horiz1)):
                if h1 < 2:
                    if (horiz1[h1] == horiz1[h1+1] == horiz1[h1+2] == horiz1[h1+3] == player): return value
            for h2 in range(len(horiz2)):
                if h2 < 2:
                    if (horiz2[h2] == horiz2[h2+1] == horiz2[h2+2] == horiz2[h2+3] == player): return value
            for h3 in range(len(horiz3)):
                if h3 < 2:
                    if (horiz3[h3] == horiz3[h3+1] == horiz3[h3+2] == horiz3[h3+3] == player): return value
            for h4 in range(len(horiz4)):
                if h4 < 2:
                    if (horiz4[h4] == horiz4[h4+1] == horiz4[h4+2] == horiz4[h4+3] == player): return value
            for v0 in range(len(vert0)):
                if v0 < 3:
                    if (vert0[v0] == vert0[v0+1] == vert0[v0+2] == vert0[v0+3] == player): return value
            for v1 in range(len(vert1)):
                if v1 < 3:
                    if (vert1[v1] == vert1[v1+1] == vert1[v1+2] == vert1[v1+3] == player): return value
            for v2 in range(len(vert2)):
                if v2 < 3:
                    if (vert2[v2] == vert2[v2+1] == vert2[v2+2] == vert2[v2+3] == player): return value
            for v3 in range(len(vert3)):
                if v3 < 3:
                    if (vert3[v3] == vert3[v3+1] == vert3[v3+2] == vert3[v3+3] == player): return value
            for v4 in range(len(vert4)):
                if v4 < 3:
                    if (vert4[v4] == vert4[v4+1] == vert4[v4+2] == vert4[v4+3] == player): return value
            for d0 in range(len(diag0)):
                if d0 < 2:
                    if (diag0[d0] == diag0[d0+1] == diag0[d0+2] == diag0[d0+3] == player): return value
            for d1 in range(len(diag1)):
                if d1 == 0:
                    if (diag1[d1] == diag1[d1+1] == diag1[d1+2] == diag1[d1+3] == player): return value            
            for d2 in range(len(diag2)):
                if d2 < 2:
                    if (diag2[d2] == diag2[d2+1] == diag2[d2+2] == diag2[d2+3] == player): return value
            for db0 in range(len(diagback0)):
                if db0 == 0:
                    if (diagback0[db0] == diagback0[db0+1] == diagback0[db0+2] == diagback0[db0+3] == player): return value
            for db1 in range(len(diagback1)):
                if db1 < 2:
                    if (diagback1[db1] == diagback1[db1+1] == diagback1[db1+2] == diagback1[db1+3] == player): return value
            for db2 in range(len(diagback2)):
                if db2 < 2:
                    if (diagback2[db2] == diagback2[db2+1] == diagback2[db2+2] == diagback2[db2+3] == player): return value
        return 0
    
    if boardsize == "1":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[5,1],state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
        vert3 = state[4,3],state[3,3],state[2,3],state[1,3],state[0,3]
        vert4 = state[4,4],state[3,4],state[2,4],state[1,4],state[0,4]
        vert5 = state[5,5],state[4,5],state[3,5],state[2,5],state[1,5],state[0,5]
        vert6 = state[5,6],state[4,6],state[3,6],state[2,6],state[1,6],state[0,6]
        horiz0 = state[0,6],state[0,5],state[0,4],state[0,3],state[0,2],state[0,1],state[0,0]
        horiz1 = state[1,6],state[1,5],state[1,4],state[1,3],state[1,2],state[1,1],state[1,0]
        horiz2 = state[2,6],state[2,5],state[2,4],state[2,3],state[2,2],state[2,1],state[2,0]
        horiz3 = state[3,6],state[3,5],state[3,4],state[3,3],state[3,2],state[3,1],state[3,0]
        horiz4 = state[4,6],state[4,5],state[4,4],state[4,3],state[4,2],state[4,1],state[4,0]
        diag0 = state[5,0],state[4,1],state[3,2],state[2,3],state[1,4],state[0,5]
        diag1 = state[5,1],state[4,2],state[3,3],state[2,4],state[1,5],state[0,6]
        diag2 = state[4,3],state[3,4],state[2,5],state[1,6]
        diag3 = state[4,0],state[3,1],state[2,2],state[1,3],state[0,4]
        diag4 = state[3,0],state[2,1],state[1,2],state[0,3]
        diagback0 = state[5,6],state[4,5],state[3,4],state[2,3],state[1,2],state[0,1]
        diagback1 = state[5,5],state[4,4],state[3,3],state[2,2],state[1,1],state[0,0]
        diagback2 = state[4,3],state[3,2],state[2,1],state[1,0]
        diagback3 = state[4,6],state[3,5],state[2,4],state[1,3],state[0,2]
        diagback4 = state[3,6],state[2,5],state[1,4],state[0,3]
    
    
        for player,value in (("X",1),("O",-1)):
            for h0 in range(len(horiz0)):
                if h0 < 4:
                    if (horiz0[h0] == horiz0[h0+1] == horiz0[h0+2] == horiz0[h0+3] == player): return value
            for h1 in range(len(horiz1)):
                if h1 < 4:
                    if (horiz1[h1] == horiz1[h1+1] == horiz1[h1+2] == horiz1[h1+3] == player): return value
            for h2 in range(len(horiz2)):
                if h2 < 4:
                    if (horiz2[h2] == horiz2[h2+1] == horiz2[h2+2] == horiz2[h2+3] == player): return value
            for h3 in range(len(horiz3)):
                if h3 < 4:
                    if (horiz3[h3] == horiz3[h3+1] == horiz3[h3+2] == horiz3[h3+3] == player): return value
            for h4 in range(len(horiz4)):
                if h4 < 4:
                    if (horiz4[h4] == horiz4[h4+1] == horiz4[h4+2] == horiz4[h4+3] == player): return value
            for v0 in range(len(vert0)):
                if v0 < 3:
                    if (vert0[v0] == vert0[v0+1] == vert0[v0+2] == vert0[v0+3] == player): return value
            for v1 in range(len(vert1)):
                if v1 < 3:
                    if (vert1[v1] == vert1[v1+1] == vert1[v1+2] == vert1[v1+3] == player): return value
            for v2 in range(len(vert2)):
                if v2 < 2:
                    if (vert2[v2] == vert2[v2+1] == vert2[v2+2] == vert2[v2+3] == player): return value
            for v3 in range(len(vert3)):
                if v3 < 2:
                    if (vert3[v3] == vert3[v3+1] == vert3[v3+2] == vert3[v3+3] == player): return value
            for v4 in range(len(vert4)):
                if v4 < 2:
                    if (vert4[v4] == vert4[v4+1] == vert4[v4+2] == vert4[v4+3] == player): return value
            for v5 in range(len(vert5)):
                if v5 < 3:
                    if (vert5[v5] == vert5[v5+1] == vert5[v5+2] == vert5[v5+3] == player): return value
            for v6 in range(len(vert6)):
                if v6 < 3:
                    if (vert6[v6] == vert6[v6+1] == vert6[v6+2] == vert6[v6+3] == player): return value
            for d0 in range(len(diag0)):
                if d0 < 3:
                    if (diag0[d0] == diag0[d0+1] == diag0[d0+2] == diag0[d0+3] == player): return value
            for d1 in range(len(diag1)):
                if d1 < 3:
                    if (diag1[d1] == diag1[d1+1] == diag1[d1+2] == diag1[d1+3] == player): return value            
            for d2 in range(len(diag2)):
                if d2 == 0:
                    if (diag2[d2] == diag2[d2+1] == diag2[d2+2] == diag2[d2+3] == player): return value
            for d3 in range(len(diag3)):
                if d3 < 1:
                    if (diag3[d3] == diag3[d3+1] == diag3[d3+2] == diag3[d3+3] == player): return value
            for d4 in range(len(diag3)):
                if d4 == 0:
                    if (diag4[d4] == diag4[d4+1] == diag4[d4+2] == diag4[d4+3] == player): return value
            for db0 in range(len(diagback0)):
                if db0 < 3:
                    if (diagback0[db0] == diagback0[db0+1] == diagback0[db0+2] == diagback0[db0+3] == player): return value
            for db1 in range(len(diagback1)):
                if db1 < 3:
                    if (diagback1[db1] == diagback1[db1+1] == diagback1[db1+2] == diagback1[db1+3] == player): return value
            for db2 in range(len(diagback2)):
                if db2 == 0:
                    if (diagback2[db2] == diagback2[db2+1] == diagback2[db2+2] == diagback2[db2+3] == player): return value
            for db3 in range(len(diagback3)):
                if db3 < 1:
                    if (diagback3[db3] == diagback3[db3+1] == diagback3[db3+2] == diagback3[db3+3] == player): return value
            for db4 in range(len(diagback4)):
                if db4 == 0:
                    if (diagback4[db4] == diagback4[db4+1] == diagback4[db4+2] == diagback4[db4+3] == player): return value
        return 0  
    
    if boardsize == "2":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[5,1],state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[5,2],state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
        vert3 = state[4,3],state[3,3],state[2,3],state[1,3],state[0,3]
        vert4 = state[4,4],state[3,4],state[2,4],state[1,4],state[0,4]
        vert5 = state[4,5],state[3,5],state[2,5],state[1,5],state[0,5]
        vert6 = state[5,6],state[4,6],state[3,6],state[2,6],state[1,6],state[0,6]
        vert7 = state[5,7],state[4,7],state[3,7],state[2,7],state[1,7],state[0,7]
        vert8 = state[5,8],state[4,8],state[3,8],state[2,8],state[1,8],state[0,8]
        horiz0 = state[0,8],state[0,7],state[0,6],state[0,5],state[0,4],state[0,3],state[0,2],state[0,1],state[0,0]
        horiz1 = state[1,8],state[1,7],state[1,6],state[1,5],state[1,4],state[1,3],state[1,2],state[1,1],state[1,0]
        horiz2 = state[2,8],state[2,7],state[2,6],state[2,5],state[2,4],state[2,3],state[2,2],state[2,1],state[2,0]
        horiz3 = state[3,8],state[3,7],state[3,6],state[3,5],state[3,4],state[3,3],state[3,2],state[3,1],state[3,0]
        horiz4 = state[4,8],state[4,7],state[4,6],state[4,5],state[4,4],state[4,3],state[4,2],state[4,1],state[4,0]
        diag0 = state[5,0],state[4,1],state[3,2],state[2,3],state[1,4],state[0,5]
        diag1 = state[5,1],state[4,2],state[3,3],state[2,4],state[1,5],state[0,6]
        diag2 = state[5,2],state[4,3],state[3,4],state[2,5],state[1,6],state[0,7]
        diag3 = state[4,4],state[3,5],state[2,6],state[1,7],state[0,8]
        diag4 = state[4,5],state[3,6],state[2,7],state[1,8]
        diag5 = state[4,0],state[3,1],state[2,2],state[1,3],state[0,4]
        diag6 = state[3,0],state[2,1],state[1,2],state[0,3]
        diagback0 = state[5,8],state[4,7],state[3,6],state[2,5],state[1,4],state[0,3]
        diagback1 = state[5,7],state[4,6],state[3,5],state[2,4],state[1,3],state[0,2]
        diagback2 = state[5,6],state[4,5],state[3,4],state[2,3],state[1,2],state[0,1]
        diagback3 = state[4,4],state[3,3],state[2,2],state[1,1],state[0,0]
        diagback4 = state[4,3],state[3,2],state[2,1],state[1,0]
        diagback5 = state[4,6],state[3,5],state[2,4],state[1,3],state[0,2]
        diagback6 = state[3,6],state[2,5],state[1,4],state[0,3]
    
    
        for player,value in (("X",1),("O",-1)):
            for h0 in range(len(horiz0)):
                if h0 < 6:
                    if (horiz0[h0] == horiz0[h0+1] == horiz0[h0+2] == horiz0[h0+3] == player): return value
            for h1 in range(len(horiz1)):
                if h1 < 6:
                    if (horiz1[h1] == horiz1[h1+1] == horiz1[h1+2] == horiz1[h1+3] == player): return value
            for h2 in range(len(horiz2)):
                if h2 < 6:
                    if (horiz2[h2] == horiz2[h2+1] == horiz2[h2+2] == horiz2[h2+3] == player): return value
            for h3 in range(len(horiz3)):
                if h3 < 6:
                    if (horiz3[h3] == horiz3[h3+1] == horiz3[h3+2] == horiz3[h3+3] == player): return value
            for h4 in range(len(horiz4)):
                if h4 < 6:
                    if (horiz4[h4] == horiz4[h4+1] == horiz4[h4+2] == horiz4[h4+3] == player): return value
            for v0 in range(len(vert0)):
                if v0 < 3:
                    if (vert0[v0] == vert0[v0+1] == vert0[v0+2] == vert0[v0+3] == player): return value
            for v1 in range(len(vert1)):
                if v1 < 3:
                    if (vert1[v1] == vert1[v1+1] == vert1[v1+2] == vert1[v1+3] == player): return value
            for v2 in range(len(vert2)):
                if v2 < 3:
                    if (vert2[v2] == vert2[v2+1] == vert2[v2+2] == vert2[v2+3] == player): return value
            for v3 in range(len(vert3)):
                if v3 < 2:
                    if (vert3[v3] == vert3[v3+1] == vert3[v3+2] == vert3[v3+3] == player): return value
            for v4 in range(len(vert4)):
                if v4 < 2:
                    if (vert4[v4] == vert4[v4+1] == vert4[v4+2] == vert4[v4+3] == player): return value
            for v5 in range(len(vert5)):
                if v5 < 2:
                    if (vert5[v5] == vert5[v5+1] == vert5[v5+2] == vert5[v5+3] == player): return value
            for v6 in range(len(vert6)):
                if v6 < 3:
                    if (vert6[v6] == vert6[v6+1] == vert6[v6+2] == vert6[v6+3] == player): return value
            for v7 in range(len(vert7)):
                if v7 < 3:
                    if (vert7[v7] == vert7[v7+1] == vert7[v7+2] == vert7[v7+3] == player): return value
            for v8 in range(len(vert8)):
                if v8 < 3:
                    if (vert8[v8] == vert8[v8+1] == vert8[v8+2] == vert8[v8+3] == player): return value
            for d0 in range(len(diag0)):
                if d0 < 3:
                    if (diag0[d0] == diag0[d0+1] == diag0[d0+2] == diag0[d0+3] == player): return value
            for d1 in range(len(diag1)):
                if d1 < 3:
                    if (diag1[d1] == diag1[d1+1] == diag1[d1+2] == diag1[d1+3] == player): return value            
            for d2 in range(len(diag2)):
                if d2 < 3:
                    if (diag2[d2] == diag2[d2+1] == diag2[d2+2] == diag2[d2+3] == player): return value
            for d3 in range(len(diag3)):
                if d3 < 2:
                    if (diag3[d3] == diag3[d3+1] == diag3[d3+2] == diag3[d3+3] == player): return value
            for d4 in range(len(diag3)):
                if d4 < 1:
                    if (diag4[d4] == diag4[d4+1] == diag4[d4+2] == diag4[d4+3] == player): return value
            for d5 in range(len(diag5)):
                if d5 < 2:
                    if (diag5[d5] == diag5[d5+1] == diag5[d5+2] == diag5[d5+3] == player): return value
            for d6 in range(len(diag6)):
                if d6 < 1:
                    if (diag6[d6] == diag6[d6+1] == diag6[d6+2] == diag6[d6+3] == player): return value
            for db0 in range(len(diagback0)):
                if db0 < 3:
                    if (diagback0[db0] == diagback0[db0+1] == diagback0[db0+2] == diagback0[db0+3] == player): return value
            for db1 in range(len(diagback1)):
                if db1 < 3:
                    if (diagback1[db1] == diagback1[db1+1] == diagback1[db1+2] == diagback1[db1+3] == player): return value
            for db2 in range(len(diagback2)):
                if db2 < 3:
                    if (diagback2[db2] == diagback2[db2+1] == diagback2[db2+2] == diagback2[db2+3] == player): return value
            for db3 in range(len(diagback3)):
                if db3 < 2:
                    if (diagback3[db3] == diagback3[db3+1] == diagback3[db3+2] == diagback3[db3+3] == player): return value
            for db4 in range(len(diagback4)):
                if db4 < 1:
                    if (diagback4[db4] == diagback4[db4+1] == diagback4[db4+2] == diagback4[db4+3] == player): return value
            for db5 in range(len(diagback5)):
                if db5 < 2:
                    if (diagback5[db5] == diagback5[db5+1] == diagback5[db5+2] == diagback5[db5+3] == player): return value
            for db6 in range(len(diagback6)):
                if db6 < 1:
                    if (diagback6[db6] == diagback6[db6+1] == diagback6[db6+2] == diagback6[db6+3] == player): return value
        return 0       
    
    if boardsize == "3":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[5,2],state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
    
        for player,value in (("X",1),("O",-1)):
            for v0 in range(len(vert0)):
                if v0 < 3:
                    if (vert0[v0] == vert0[v0+1] == vert0[v0+2] == vert0[v0+3] == player): return value
            for v1 in range(len(vert1)):
                if v1 < 2:
                    if (vert1[v1] == vert1[v1+1] == vert1[v1+2] == vert1[v1+3] == player): return value
            for v2 in range(len(vert2)):
                if v2 < 3:
                    if (vert2[v2] == vert2[v2+1] == vert2[v2+2] == vert2[v2+3] == player): return value
        return 0
def get_player(state):
    return "XO"[
        np.count_nonzero(state == "O") < np.count_nonzero(state == "X")]

def children_of(state):
    symbol = get_player(state)
    children = []
    for r in range(state.shape[0]):
        for c in range(state.shape[1]):
            if (state[r,c] == "_") and ((r+1 == 6) or (state[r+1,c] == "X") or (state[r+1,c] == "O")):
                child = state.copy()
                child[r,c] = symbol
                children.append(child)
    return list(reversed(children))

def depth_limited_minimax(state, max_depth, evaluate, boardsize):
    # returns chosen child state, utility
    player = get_player(state)
    children = children_of(state)
    value = score(state,boardsize)

    # base cases
    if len(children) == 0 or value != 0: return None, value
    if max_depth == 0: return None, evaluate(state)

    # recursive case
    results = [
        depth_limited_minimax(child, max_depth-1, evaluate, boardsize)
        for child in children]

    _, utilities = zip(*results)
    if player == "X": action = np.argmax(utilities)
    if player == "O": action = np.argmin(utilities)
    return children[action], utilities[action]

def evaluate(state):
    count = 0
    if boardsize == "0":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
        vert3 = state[4,3],state[3,3],state[2,3],state[1,3],state[0,3]
        vert4 = state[5,4],state[4,4],state[3,4],state[2,4],state[1,4],state[0,4]
        horiz0 = state[0,4],state[0,3],state[0,2],state[0,1],state[0,0]
        horiz1 = state[1,4],state[1,3],state[1,2],state[1,1],state[1,0]
        horiz2 = state[2,4],state[2,3],state[2,2],state[2,1],state[2,0]
        horiz3 = state[3,4],state[3,3],state[3,2],state[3,1],state[3,0]
        horiz4 = state[4,4],state[4,3],state[4,2],state[4,1],state[4,0]
        diag0 = state[5,0],state[4,1],state[3,2],state[2,3],state[1,4]
        diag1 = state[4,0],state[3,1],state[2,2],state[1,3],state[0,4]
        diag2 = state[3,0],state[2,1],state[1,2],state[0,3]
        diagback0 = state[3,4],state[2,3],state[1,2],state[0,1]
        diagback1 = state[4,4],state[3,3],state[2,2],state[1,1],state[0,0]
        diagback2 = state[5,4],state[4,3],state[3,2],state[2,1],state[1,0]
    
    
        for player,value in (("X",1),("O",-1)):
            for h0 in range(len(horiz0)):
                if h0 < 2:
                    if ((horiz0[h0] == horiz0[h0+1] == horiz0[h0+2] == player) and (horiz0[h0+3] == "_")) or ((horiz0[h0] == player) and horiz0[h0+1] == "_" and horiz0[h0+2] == "_" and horiz0[h0+3] == "_"): count = count+1
            for h1 in range(len(horiz1)):
                if h1 < 2:
                    if ((horiz1[h1] == horiz1[h1+1] == horiz1[h1+2] == player) and (horiz1[h1+3] == "_")) or ((horiz1[h1] == player) and horiz1[h1+1] == "_" and horiz1[h1+2] == "_" and horiz1[h1+3] == "_"): count = count+1
            for h2 in range(len(horiz2)):
                if h2 < 2:
                    if ((horiz2[h2] == horiz2[h2+1] == horiz2[h2+2] == player) and (horiz2[h2+3] == "_")) or ((horiz2[h2] == player) and horiz2[h2+1] == "_" and horiz2[h2+2] == "_" and horiz2[h2+3] == "_"): count = count+1
            for h3 in range(len(horiz3)):
                if h3 < 2:
                    if ((horiz3[h3] == horiz3[h3+1] == horiz3[h3+2] == player) and (horiz3[h3+3] == "_")) or ((horiz3[h3] == player) and horiz3[h3+1] == "_" and horiz3[h3+2] == "_" and horiz3[h3+3] == "_"): count = count+1
            for h4 in range(len(horiz4)):
                if h4 < 2:
                    if ((horiz4[h4] == horiz4[h4+1] == horiz4[h4+2] == player) and (horiz4[h4+3] == "_")) or ((horiz4[h4] == player) and horiz4[h4+1] == "_" and horiz4[h4+2] == "_" and horiz4[h4+3] == "_"): count = count+1
            for v0 in range(len(vert0)):
                if v0 < 3:
                    if ((vert0[v0] == vert0[v0+1] == vert0[v0+2] == player) and (vert0[v0+3] == "_")) or ((vert0[v0] == player) and vert0[v0+1] == "_" and vert0[v0+2] == "_" and vert0[v0+3] == "_"): count = count+1
            for v1 in range(len(vert1)):
                if v1 < 3:
                    if ((vert1[v1] == vert1[v1+1] == vert1[v1+2] == player) and (vert1[v1+3] == "_")) or ((vert1[v1] == player) and vert1[v1+1] == "_" and vert1[v1+2] == "_" and vert1[v1+3] == "_"): count = count+1
            for v2 in range(len(vert2)):
                if v2 < 3:
                    if ((vert2[v2] == vert2[v2+1] == vert2[v2+2] == player) and (vert2[v2+3] == "_")) or ((vert2[v2] == player) and vert2[v2+1] == "_" and vert2[v2+2] == "_" and vert2[v2+3] == "_"): count = count+1
            for v3 in range(len(vert3)):
                if v3 < 3:
                    if ((vert3[v3] == vert3[v3+1] == vert3[v3+2] == player) and (vert3[v3+3] == "_")) or ((vert3[v3] == player) and vert3[v3+1] == "_" and vert3[v3+2] == "_" and vert3[v3+3] == "_"): count = count+1
            for v4 in range(len(vert4)):
                if v4 < 3:
                    if ((vert4[v4] == vert4[v4+1] == vert4[v4+2] == player) and (vert4[v4+3] == "_")) or ((vert4[v4] == player) and vert4[v4+1] == "_" and vert4[v4+2] == "_" and vert4[v4+3] == "_"): count = count+1
            for d0 in range(len(diag0)):
                if d0 < 2:
                    if ((diag0[d0] == diag0[d0+1] == diag0[d0+2] == player) and (diag0[d0+3] == "_")) or ((diag0[d0] == player) and diag0[d0+1] == "_" and diag0[d0+2] == "_" and diag0[d0+3] == "_"): count = count+1
            for d1 in range(len(diag1)):
                if d1 == 0:
                    if ((diag1[d1] == diag1[d1+1] == diag1[d1+2] == player) and (diag0[d0+3] == "_")) or ((diag1[d1] == player) and diag1[d1+1] == "_" and diag1[d1+2] == "_" and diag1[d1+3] == "_"): count = count+1            
            for d2 in range(len(diag2)):
                if d2 < 2:
                    if ((diag2[d2] == diag2[d2+1] == diag2[d2+2] == player) and (diag0[d0+3] == "_")) or ((diag2[d2] == player) and diag2[d2+1] == "_" and diag2[d2+2] == "_" and diag2[d2+3] == "_"): count = count+1
            for db0 in range(len(diagback0)):
                if db0 == 0:
                    if ((diagback0[db0] == diagback0[db0+1] == diagback0[db0+2] == player) and (diagback0[db0+3] == "_")) or ((diagback0[db0] == player) and diagback0[db0+1] == "_" and diagback0[db0+2] == "_" and diagback0[db0+3] == "_"): count = count+1
            for db1 in range(len(diagback1)):
                if db1 < 2:
                    if ((diagback1[db1] == diagback1[db1+1] == diagback1[db1+2] == player) and (diagback1[db1+3] == "_")) or ((diagback1[db1] == player) and diagback1[db1+1] == "_" and diagback1[db1+2] == "_" and diagback1[db1+3] == "_"): count = count+1
            for db2 in range(len(diagback2)):
                if db2 < 2:
                    if ((diagback2[db2] == diagback2[db2+1] == diagback2[db2+2] == player) and (diagback2[db2+3] == "_")) or ((diagback2[db2] == player) and diagback2[db2+1] == "_" and diagback2[db2+2] == "_" and diagback2[db2+3] == "_"): count = count+1
        return count*value
    
    if boardsize == "1":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[5,1],state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
        vert3 = state[4,3],state[3,3],state[2,3],state[1,3],state[0,3]
        vert4 = state[4,4],state[3,4],state[2,4],state[1,4],state[0,4]
        vert5 = state[5,5],state[4,5],state[3,5],state[2,5],state[1,5],state[0,5]
        vert6 = state[5,6],state[4,6],state[3,6],state[2,6],state[1,6],state[0,6]
        horiz0 = state[0,6],state[0,5],state[0,4],state[0,3],state[0,2],state[0,1],state[0,0]
        horiz1 = state[1,6],state[1,5],state[1,4],state[1,3],state[1,2],state[1,1],state[1,0]
        horiz2 = state[2,6],state[2,5],state[2,4],state[2,3],state[2,2],state[2,1],state[2,0]
        horiz3 = state[3,6],state[3,5],state[3,4],state[3,3],state[3,2],state[3,1],state[3,0]
        horiz4 = state[4,6],state[4,5],state[4,4],state[4,3],state[4,2],state[4,1],state[4,0]
        diag0 = state[5,0],state[4,1],state[3,2],state[2,3],state[1,4],state[0,5]
        diag1 = state[5,1],state[4,2],state[3,3],state[2,4],state[1,5],state[0,6]
        diag2 = state[4,3],state[3,4],state[2,5],state[1,6]
        diag3 = state[4,0],state[3,1],state[2,2],state[1,3],state[0,4]
        diag4 = state[3,0],state[2,1],state[1,2],state[0,3]
        diagback0 = state[5,6],state[4,5],state[3,4],state[2,3],state[1,2],state[0,1]
        diagback1 = state[5,5],state[4,4],state[3,3],state[2,2],state[1,1],state[0,0]
        diagback2 = state[4,3],state[3,2],state[2,1],state[1,0]
        diagback3 = state[4,6],state[3,5],state[2,4],state[1,3],state[0,2]
        diagback4 = state[3,6],state[2,5],state[1,4],state[0,3]
    
    
        for player,value in (("X",1),("O",-1)):
            for h0 in range(len(horiz0)):
                if h0 < 4:
                    if ((horiz0[h0] == horiz0[h0+1] == horiz0[h0+2] == player) and (horiz0[h0+3] == "_")) or ((horiz0[h0] == player) and horiz0[h0+1] == "_" and horiz0[h0+2] == "_" and horiz0[h0+3] == "_"): count = count+1
            for h1 in range(len(horiz1)):
                if h1 < 4:
                    if ((horiz1[h1] == horiz1[h1+1] == horiz1[h1+2] == player) and (horiz1[h1+3] == "_")) or ((horiz1[h1] == player) and horiz1[h1+1] == "_" and horiz1[h1+2] == "_" and horiz1[h1+3] == "_"): count = count+1
            for h2 in range(len(horiz2)):
                if h2 < 4:
                    if ((horiz2[h2] == horiz2[h2+1] == horiz2[h2+2] == player) and (horiz2[h2+3] == "_")) or ((horiz2[h2] == player) and horiz2[h2+1] == "_" and horiz2[h2+2] == "_" and horiz2[h2+3] == "_"): count = count+1
            for h3 in range(len(horiz3)):
                if h3 < 4:
                    if ((horiz3[h3] == horiz3[h3+1] == horiz3[h3+2] == player) and (horiz3[h3+3] == "_")) or ((horiz3[h3] == player) and horiz3[h3+1] == "_" and horiz3[h3+2] == "_" and horiz3[h3+3] == "_"): count = count+1
            for h4 in range(len(horiz4)):
                if h4 < 4:
                    if ((horiz4[h4] == horiz4[h4+1] == horiz4[h4+2] == player) and (horiz4[h4+3] == "_")) or ((horiz4[h4] == player) and horiz4[h4+1] == "_" and horiz4[h4+2] == "_" and horiz4[h4+3] == "_"): count = count+1
            for v0 in range(len(vert0)):
                if v0 < 3:
                    if ((vert0[v0] == vert0[v0+1] == vert0[v0+2] == player) and (vert0[v0+3] == "_")) or ((vert0[v0] == player) and vert0[v0+1] == "_" and vert0[v0+2] == "_" and vert0[v0+3] == "_"): count = count+1
            for v1 in range(len(vert1)):
                if v1 < 3:
                    if ((vert1[v1] == vert1[v1+1] == vert1[v1+2] == player) and (vert1[v1+3] == "_")) or ((vert1[v1] == player) and vert1[v1+1] == "_" and vert1[v1+2] == "_" and vert1[v1+3] == "_"): count = count+1
            for v2 in range(len(vert2)):
                if v2 < 2:
                    if ((vert2[v2] == vert2[v2+1] == vert2[v2+2] == player) and (vert2[v2+3] == "_")) or ((vert2[v2] == player) and vert2[v2+1] == "_" and vert2[v2+2] == "_" and vert2[v2+3] == "_"): count = count+1
            for v3 in range(len(vert3)):
                if v3 < 2:
                    if ((vert3[v3] == vert3[v3+1] == vert3[v3+2] == player) and (vert3[v3+3] == "_")) or ((vert3[v3] == player) and vert3[v3+1] == "_" and vert3[v3+2] == "_" and vert3[v3+3] == "_"): count = count+1
            for v4 in range(len(vert4)):
                if v4 < 2:
                    if ((vert4[v4] == vert4[v4+1] == vert4[v4+2] == player) and (vert4[v4+3] == "_")) or ((vert4[v4] == player) and vert4[v4+1] == "_" and vert4[v4+2] == "_" and vert4[v4+3] == "_"): count = count+1
            for v5 in range(len(vert5)):
                if v5 < 3:
                    if ((vert5[v5] == vert5[v5+1] == vert5[v5+2] == player) and (vert5[v5+3] == "_")) or ((vert5[v5] == player) and vert5[v5+1] == "_" and vert5[v5+2] == "_" and vert5[v5+3] == "_"): count = count+1
            for v6 in range(len(vert6)):
                if v6 < 3:
                    if ((vert6[v6] == vert6[v6+1] == vert6[v6+2] == player) and (vert6[v6+3] == "_")) or ((vert6[v6] == player) and vert6[v6+1] == "_" and vert6[v6+2] == "_" and vert6[v6+3] == "_"): count = count+1
            for d0 in range(len(diag0)):
                if d0 < 3:
                    if ((diag0[d0] == diag0[d0+1] == diag0[d0+2] == player) and (diag0[d0+3] == "_")) or ((diag0[d0] == player) and diag0[d0+1] == "_" and diag0[d0+2] == "_" and diag0[d0+3] == "_"): count = count+1
            for d1 in range(len(diag1)):
                if d1 < 3:
                    if ((diag1[d1] == diag1[d1+1] == diag1[d1+2] == player) and (diag1[d1+3] == "_")) or ((diag1[d1] == player) and diag1[d1+1] == "_" and diag1[d1+2] == "_" and diag1[d1+3] == "_"): count = count+1            
            for d2 in range(len(diag2)):
                if d2 == 0:
                    if ((diag2[d2] == diag2[d2+1] == diag2[d2+2] == player) and (diag2[d2+3] == "_")) or ((diag2[d2] == player) and diag2[d2+1] == "_" and diag2[d2+2] == "_" and diag2[d2+3] == "_"): count = count+1
            for d3 in range(len(diag3)):
                if d3 < 1:
                    if ((diag3[d3] == diag3[d3+1] == diag3[d3+2] == player) and (diag3[d3+3] == "_")) or ((diag3[d3] == player) and diag3[d3+1] == "_" and diag3[d3+2] == "_" and diag3[d3+3] == "_"): count = count+1
            for d4 in range(len(diag3)):
                if d4 == 0:
                    if ((diag4[d4] == diag4[d4+1] == diag4[d4+2] == player) and (diag4[d4+3] == "_")) or ((diag4[d4] == player) and diag4[d4+1] == "_" and diag4[d4+2] == "_" and diag4[d4+3] == "_"): count = count+1
            for db0 in range(len(diagback0)):
                if db0 < 3:
                    if ((diagback0[db0] == diagback0[db0+1] == diagback0[db0+2] == player) and (diagback0[db0+3] == "_")) or ((diagback0[db0] == player) and diagback0[db0+1] == "_" and diagback0[db0+2] == "_" and diagback0[db0+3] == "_"): count = count+1
            for db1 in range(len(diagback1)):
                if db1 < 3:
                    if ((diagback1[db1] == diagback1[db1+1] == diagback1[db1+2] == player) and (diagback1[db1+3] == "_")) or ((diagback1[db1] == player) and diagback1[db1+1] == "_" and diagback1[db1+2] == "_" and diagback1[db1+3] == "_"): count = count+1
            for db2 in range(len(diagback2)):
                if db2 == 0:
                    if ((diagback2[db2] == diagback2[db2+1] == diagback2[db2+2] == player) and (diagback2[db2+3] == "_")) or ((diagback2[db2] == player) and diagback2[db2+1] == "_" and diagback2[db2+2] == "_" and diagback2[db2+3] == "_"): count = count+1
            for db3 in range(len(diagback3)):
                if db3 < 1:
                    if ((diagback3[db3] == diagback3[db3+1] == diagback3[db3+2] == player) and (diagback3[db3+3] == "_")) or ((diagback3[db3] == player) and diagback3[db3+1] == "_" and diagback3[db3+2] == "_" and diagback3[db3+3] == "_"): count = count+1
            for db4 in range(len(diagback4)):
                if db4 == 0:
                    if ((diagback4[db4] == diagback4[db4+1] == diagback4[db4+2] == player) and (diagback4[db4+3] == "_")) or ((diagback4[db4] == player) and diagback4[db4+1] == "_" and diagback4[db4+2] == "_" and diagback4[db4+3] == "_"): count = count+1
        return count*value  
    
    if boardsize == "2":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[5,1],state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[5,2],state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
        vert3 = state[4,3],state[3,3],state[2,3],state[1,3],state[0,3]
        vert4 = state[4,4],state[3,4],state[2,4],state[1,4],state[0,4]
        vert5 = state[4,5],state[3,5],state[2,5],state[1,5],state[0,5]
        vert6 = state[5,6],state[4,6],state[3,6],state[2,6],state[1,6],state[0,6]
        vert7 = state[5,7],state[4,7],state[3,7],state[2,7],state[1,7],state[0,7]
        vert8 = state[5,8],state[4,8],state[3,8],state[2,8],state[1,8],state[0,8]
        horiz0 = state[0,8],state[0,7],state[0,6],state[0,5],state[0,4],state[0,3],state[0,2],state[0,1],state[0,0]
        horiz1 = state[1,8],state[1,7],state[1,6],state[1,5],state[1,4],state[1,3],state[1,2],state[1,1],state[1,0]
        horiz2 = state[2,8],state[2,7],state[2,6],state[2,5],state[2,4],state[2,3],state[2,2],state[2,1],state[2,0]
        horiz3 = state[3,8],state[3,7],state[3,6],state[3,5],state[3,4],state[3,3],state[3,2],state[3,1],state[3,0]
        horiz4 = state[4,8],state[4,7],state[4,6],state[4,5],state[4,4],state[4,3],state[4,2],state[4,1],state[4,0]
        diag0 = state[5,0],state[4,1],state[3,2],state[2,3],state[1,4],state[0,5]
        diag1 = state[5,1],state[4,2],state[3,3],state[2,4],state[1,5],state[0,6]
        diag2 = state[5,2],state[4,3],state[3,4],state[2,5],state[1,6],state[0,7]
        diag3 = state[4,4],state[3,5],state[2,6],state[1,7],state[0,8]
        diag4 = state[4,5],state[3,6],state[2,7],state[1,8]
        diag5 = state[4,0],state[3,1],state[2,2],state[1,3],state[0,4]
        diag6 = state[3,0],state[2,1],state[1,2],state[0,3]
        diagback0 = state[5,8],state[4,7],state[3,6],state[2,5],state[1,4],state[0,3]
        diagback1 = state[5,7],state[4,6],state[3,5],state[2,4],state[1,3],state[0,2]
        diagback2 = state[5,6],state[4,5],state[3,4],state[2,3],state[1,2],state[0,1]
        diagback3 = state[4,4],state[3,3],state[2,2],state[1,1],state[0,0]
        diagback4 = state[4,3],state[3,2],state[2,1],state[1,0]
        diagback5 = state[4,6],state[3,5],state[2,4],state[1,3],state[0,2]
        diagback6 = state[3,6],state[2,5],state[1,4],state[0,3]
    
    
        for player,value in (("X",1),("O",-1)):
            for h0 in range(len(horiz0)):
                if h0 < 6:
                    if ((horiz0[h0] == horiz0[h0+1] == horiz0[h0+2] == player) and (horiz0[h0+3] == "_")) or ((horiz0[h0] == player) and horiz0[h0+1] == "_" and horiz0[h0+2] == "_" and horiz0[h0+3] == "_"): count = count+1
            for h1 in range(len(horiz1)):
                if h1 < 6:
                    if ((horiz1[h1] == horiz1[h1+1] == horiz1[h1+2] == player) and (horiz1[h1+3] == "_")) or ((horiz1[h1] == player) and horiz1[h1+1] == "_" and horiz1[h1+2] == "_" and horiz1[h1+3] == "_"): count = count+1
            for h2 in range(len(horiz2)):
                if h2 < 6:
                    if ((horiz2[h2] == horiz2[h2+1] == horiz2[h2+2] == player) and (horiz2[h2+3] == "_")) or ((horiz2[h2] == player) and horiz2[h2+1] == "_" and horiz2[h2+2] == "_" and horiz2[h2+3] == "_"): count = count+1
            for h3 in range(len(horiz3)):
                if h3 < 6:
                    if ((horiz3[h3] == horiz3[h3+1] == horiz3[h3+2] == player) and (horiz3[h3+3] == "_")) or ((horiz3[h3] == player) and horiz3[h3+1] == "_" and horiz3[h3+2] == "_" and horiz3[h3+3] == "_"): count = count+1
            for h4 in range(len(horiz4)):
                if h4 < 6:
                    if ((horiz4[h4] == horiz4[h4+1] == horiz4[h4+2] == player) and (horiz4[h4+3] == "_")) or ((horiz4[h4] == player) and horiz4[h4+1] == "_" and horiz4[h4+2] == "_" and horiz4[h4+3] == "_"): count = count+1
            for v0 in range(len(vert0)):
                if v0 < 3:
                    if ((vert0[v0] == vert0[v0+1] == vert0[v0+2] == player) and (vert0[v0+3] == "_")) or ((vert0[v0] == player) and vert0[v0+1] == "_" and vert0[v0+2] == "_" and vert0[v0+3] == "_"): count = count+1
            for v1 in range(len(vert1)):
                if v1 < 3:
                    if ((vert1[v1] == vert1[v1+1] == vert1[v1+2] == player) and (vert1[v1+3] == "_")) or ((vert1[v1] == player) and vert1[v1+1] == "_" and vert1[v1+2] == "_" and vert1[v1+3] == "_"): count = count+1
            for v2 in range(len(vert2)):
                if v2 < 3:
                    if ((vert2[v2] == vert2[v2+1] == vert2[v2+2] == player) and (vert2[v2+3] == "_")) or ((vert2[v2] == player) and vert2[v2+1] == "_" and vert2[v2+2] == "_" and vert2[v2+3] == "_"): count = count+1
            for v3 in range(len(vert3)):
                if v3 < 2:
                    if ((vert3[v3] == vert3[v3+1] == vert3[v3+2] == player) and (vert3[v3+3] == "_")) or ((vert3[v3] == player) and vert3[v3+1] == "_" and vert3[v3+2] == "_" and vert3[v3+3] == "_"): count = count+1
            for v4 in range(len(vert4)):
                if v4 < 2:
                    if ((vert4[v4] == vert4[v4+1] == vert4[v4+2] == player) and (vert4[v4+3] == "_")) or ((vert4[v4] == player) and vert4[v4+1] == "_" and vert4[v4+2] == "_" and vert4[v4+3] == "_"): count = count+1
            for v5 in range(len(vert5)):
                if v5 < 2:
                    if ((vert5[v5] == vert5[v5+1] == vert5[v5+2] == player) and (vert5[v5+3] == "_")) or ((vert5[v5] == player) and vert5[v5+1] == "_" and vert5[v5+2] == "_" and vert5[v5+3] == "_"): count = count+1
            for v6 in range(len(vert6)):
                if v6 < 3:
                    if ((vert6[v6] == vert6[v6+1] == vert6[v6+2] == player) and (vert6[v6+3] == "_")) or ((vert6[v6] == player) and vert6[v6+1] == "_" and vert6[v6+2] == "_" and vert6[v6+3] == "_"): count = count+1
            for v7 in range(len(vert7)):
                if v7 < 3:
                    if ((vert7[v7] == vert7[v7+1] == vert7[v7+2] == player) and (vert7[v7+3] == "_")) or ((vert7[v7] == player) and vert7[v7+1] == "_" and vert7[v7+2] == "_" and vert7[v7+3] == "_"): count = count+1
            for v8 in range(len(vert8)):
                if v8 < 3:
                    if ((vert8[v8] == vert8[v8+1] == vert8[v8+2] == player) and (vert8[v8+3] == "_")) or ((vert8[v8] == player) and vert8[v8+1] == "_" and vert8[v8+2] == "_" and vert8[v8+3] == "_"): count = count+1
            for d0 in range(len(diag0)):
                if d0 < 3:
                    if ((diag0[d0] == diag0[d0+1] == diag0[d0+2] == player) and (diag0[d0+3] == "_")) or ((diag0[d0] == player) and diag0[d0+1] == "_" and diag0[d0+2] == "_" and diag0[d0+3] == "_"): count = count+1
            for d1 in range(len(diag1)):
                if d1 < 3:
                    if ((diag1[d1] == diag1[d1+1] == diag1[d1+2] == player) and (diag1[d1+3] == "_")) or ((diag1[d1] == player) and diag1[d1+1] == "_" and diag1[d1+2] == "_" and diag1[d1+3] == "_"): count = count+1            
            for d2 in range(len(diag2)):
                if d2 < 3:
                    if ((diag2[d2] == diag2[d2+1] == diag2[d2+2] == player) and (diag2[d2+3] == "_")) or ((diag2[d2] == player) and diag2[d2+1] == "_" and diag2[d2+2] == "_" and diag2[d2+3] == "_"): count = count+1
            for d3 in range(len(diag3)):
                if d3 < 2:
                    if ((diag3[d3] == diag3[d3+1] == diag3[d3+2] == player) and (diag3[d3+3] == "_")) or ((diag3[d3] == player) and diag3[d3+1] == "_" and diag3[d3+2] == "_" and diag3[d3+3] == "_"): count = count+1
            for d4 in range(len(diag3)):
                if d4 < 1:
                    if ((diag4[d4] == diag4[d4+1] == diag4[d4+2] == player) and (diag4[d4+3] == "_")) or ((diag4[d4] == player) and diag4[d4+1] == "_" and diag4[d4+2] == "_" and diag4[d4+3] == "_"): count = count+1
            for d5 in range(len(diag5)):
                if d5 < 2:
                    if ((diag5[d5] == diag5[d5+1] == diag5[d5+2] == player) and (diag5[d5+3] == "_")) or ((diag5[d5] == player) and diag5[d5+1] == "_" and diag5[d5+2] == "_" and diag5[d5+3] == "_"): count = count+1
            for d6 in range(len(diag6)):
                if d6 < 1:
                    if ((diag6[d6] == diag6[d6+1] == diag6[d6+2] == player) and (diag6[d6+3] == "_")) or ((diag6[d6] == player) and diag6[d6+1] == "_" and diag6[d6+2] == "_" and diag6[d6+3] == "_"): count = count+1
            for db0 in range(len(diagback0)):
                if db0 < 3:
                    if ((diagback0[db0] == diagback0[db0+1] == diagback0[db0+2] == player) and (diagback0[db0+3] == "_")) or ((diagback0[db0] == player) and diagback0[db0+1] == "_" and diagback0[db0+2] == "_" and diagback0[db0+3] == "_"): count = count+1
            for db1 in range(len(diagback1)):
                if db1 < 3:
                    if ((diagback1[db1] == diagback1[db1+1] == diagback1[db1+2] == player) and (diagback1[db1+3] == "_")) or ((diagback1[db1] == player) and diagback1[db1+1] == "_" and diagback1[db1+2] == "_" and diagback1[db1+3] == "_"): count = count+1
            for db2 in range(len(diagback2)):
                if db2 < 3:
                    if ((diagback2[db2] == diagback2[db2+1] == diagback2[db2+2] == player) and (diagback2[db2+3] == "_")) or ((diagback2[db2] == player) and diagback2[db2+1] == "_" and diagback2[db2+2] == "_" and diagback2[db2+3] == "_"): count = count+1
            for db3 in range(len(diagback3)):
                if db3 < 2:
                    if ((diagback3[db3] == diagback3[db3+1] == diagback3[db3+2] == player) and (diagback3[db3+3] == "_")) or ((diagback3[db3] == player) and diagback3[db3+1] == "_" and diagback3[db3+2] == "_" and diagback3[db3+3] == "_"): count = count+1
            for db4 in range(len(diagback4)):
                if db4 < 1:
                    if ((diagback4[db4] == diagback4[db4+1] == diagback4[db4+2] == player) and (diagback4[db4+3] == "_")) or ((diagback4[db4] == player) and diagback4[db4+1] == "_" and diagback4[db4+2] == "_" and diagback4[db4+3] == "_"): count = count+1
            for db5 in range(len(diagback5)):
                if db5 < 2:
                    if ((diagback5[db5] == diagback5[db5+1] == diagback5[db5+2] == player) and (diagback5[db5+3] == "_")) or ((diagback5[db5] == player) and diagback5[db5+1] == "_" and diagback5[db5+2] == "_" and diagback5[db5+3] == "_"): count = count+1
            for db6 in range(len(diagback6)):
                if db6 < 1:
                    if ((diagback6[db6] == diagback6[db6+1] == diagback6[db6+2] == player) and (diagback6[db6+3] == "_")) or ((diagback6[db6] == player) and diagback6[db6+1] == "_" and diagback6[db6+2] == "_" and diagback6[db6+3] == "_"): count = count+1
        return count*value
    
    if boardsize == "3":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[5,2],state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
    
        for player,value in (("X",1),("O",-1)):
            for v0 in range(len(vert0)):
                if v0 < 3:
                    if ((vert0[v0] == vert0[v0+1] == vert0[v0+2] == player) and (vert0[v0+3] == "_")) or ((vert0[v0] == player) and vert0[v0+1] == "_" and vert0[v0+2] == "_" and vert0[v0+3] == "_"): count = count+1
            for v1 in range(len(vert1)):
                if v1 < 2:
                    if ((vert1[v1] == vert1[v1+1] == vert1[v1+2] == player) and (vert1[v1+3] == "_")) or ((vert1[v1] == player) and vert1[v1+1] == "_" and vert1[v1+2] == "_" and vert1[v1+3] == "_"): count = count+1
            for v2 in range(len(vert2)):
                if v2 < 3:
                    if ((vert2[v2] == vert2[v2+1] == vert2[v2+2] == player) and (vert2[v2+3] == "_")) or ((vert2[v2] == player) and vert2[v2+1] == "_" and vert2[v2+2] == "_" and vert2[v2+3] == "_"): count = count+1
        return count*value   
         
#EVERYTHING BELOW THIS LINE IS COPIED AND/OR MODIFIED FROM https://colab.research.google.com/drive/1YR8HjSw8K0n684S_oGnZPpU69SmOw355?usp=sharing#scrollTo=Gt28shQVGszO
#AUTHORED BY DR. GARRET KATZ AT SYRACUSE UNIVERSITY
# Code to generate training data
# Each training example is an intermediate game state, paired with its minimax value

# Used to get a random state somewhere in the game tree for a training example
# Performs random actions for the given number of turns (depth parameter)
def valid_actions(state):
    actions = list()
    for r in range(state.shape[0]):
        for c in range(state.shape[1]):
            if (state[r,c] == "_") and ((r+1 == 6) or (state[r+1,c] == "X") or (state[r+1,c] == "O")):
                actions.append((r,c))
                np.array(actions)
    return actions


def random_state(depth, boardsize):
    if boardsize == "0":
        state = np.array([["_"]*5]*6)
    if boardsize == "1":
        state = np.array([["_"]*7]*6)
    if boardsize == "2":
        state = np.array([["_"]*9]*6)
    if boardsize == "3":
        state = np.array([["_"]*3]*6)
    for d in range(depth):
        actions = valid_actions(state)
        if len(actions) == 0: break
        action = actions[np.random.randint(len(actions))]
        row, col = action
        player =  get_player(state)
        state[row,col] = player
        new_state = state
        new_state[row, col] = player
    return state

# Used to generate a training data set
# Samples random states at a given depth and then calculates their minimax value
def generate(state,evaluate,boardsize,num_examples,depth):
    examples = []
    for n in range(num_examples):
        state = random_state(depth, boardsize)
        children,utility = depth_limited_minimax(state, depth, evaluate,boardsize)
        examples.append((state, utility))
    return examples

# Augment data with rotations and reflections
def augment(examples):
    max_depth = 0
    augmented = []
    for state, utility in examples:
        for r in range(state.shape[0]):
            for c in range(state.shape[1]):
                if state[r,c] == "X":
                    state[r,c] = "_"
                if state[r,c] == "O":
                    state[r,c] = "X"
                if state[r,c] == "_":
                    state[r,c] = "O"
                children,utility = depth_limited_minimax(state, max_depth, evaluate, boardsize)
                augmented.append((state,utility))
    return augmented


# Used to convert a game state to a tensor encoding suitable for NN input
# Uses one-hot encoding at each grid position
def encode(state):
    # encoding[0,:,:] == 1 where there are "_"s, 0 elsewhere
    # encoding[1,:,:] == 1 where there are "O"s, 0 elsewhere
    # encoding[2,:,:] == 1 where there are "X"s, 0 elsewhere
    symbols = np.array(["_","O","X"]).reshape(-1,1,1)
    onehot = (symbols == state).astype(np.float32)
    return tr.tensor(onehot)

# Generate a lot of training/testing data
boardsize = det_board_size()
if boardsize == "0":
    state = np.array([["_"]*5]*6)
    print(state)
if boardsize == "1":
    state = np.array([["_"]*7]*6)
    print(state)
if boardsize == "2":
    state = np.array([["_"]*9]*6)
    print(state)
if boardsize == "3":
    state = np.array([["_"]*3]*6)
    print(state)
    
training_examples = generate(state, evaluate, boardsize, num_examples = 50, depth = 42)
testing_examples = generate(state, evaluate, boardsize, num_examples = 50, depth = 42)

# augment training data
print(len(training_examples))
#print(training_examples)
training_examples = augment(training_examples)
print(len(training_examples))
#print(training_examples)

# Baseline testing error: always predict 0 for minimax result
_, utilities = zip(*testing_examples)
baseline_error =sum(u**2 for u in utilities) / len(utilities)


if boardsize == "0":
    size1 = 6
    size2 = 5
if boardsize == "1":
    size1 = 6
    size2 = 7
if boardsize == "2":
    size1 = 6
    size2 = 9
if boardsize == "3":
    size1 = 6
    size2 = 3

# Defines a network with two fully-connected layers and tanh activation functions
class LinNet(tr.nn.Module):
    def __init__(self, size1, size2, hid_features):
        super(LinNet, self).__init__()
        self.to_hidden = tr.nn.Linear(3*size1*size2, hid_features)
        self.to_output = tr.nn.Linear(hid_features, 1)
    def forward(self, x):
        h = tr.relu(self.to_hidden(x.reshape(x.shape[0],-1)))
        y = tr.tanh(self.to_output(h))
        return y


net = LinNet(size1, size2, hid_features=8)
print(net)
    

# Calculates the error on one training example
def example_error(net, example):
    state, utility = example
    x = encode(state).unsqueeze(0)
    y = net(x)
    e = (y - utility)**2
    return e

# Calculates the error on a batch of training examples
def batch_error(net, batch):
    states, utilities = batch
    u = utilities.reshape(-1,1).float()
    y = net(states)
    e = tr.sum((y - u)**2) / utilities.shape[0]
    return e

# Trains the network on some generated data
if __name__ == "__main__":

    # whether to loop over individual training examples or batch them
    batched = True


    net = LinNet(size1, size2, hid_features=4)
    optimizer = tr.optim.SGD(net.parameters(), lr=0.00001, momentum=0.9)

    # Convert the states and their minimax utilities to tensors
    states, utilities = zip(*training_examples)
    training_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)

    states, utilities = zip(*testing_examples)
    testing_batch = tr.stack(tuple(map(encode, states))), tr.tensor(utilities)

    # Run the gradient descent iterations
    curves = [], []
    for epoch in range(50000):
    
        # zero out the gradients for the next backward pass
        optimizer.zero_grad()

        # loop version (slow)
        if not batched:
 
            training_error, testing_error = 0, 0

            for n, example in enumerate(training_examples):
                e = example_error(net, example)
                e.backward()
                training_error += e.item()
            training_error /= len(training_examples)

            with tr.no_grad(): # less computationally expensive
                for n, example in enumerate(testing_examples):
                    e = example_error(net, example)
                    testing_error += e.item()
                testing_error /= len(testing_examples)

        # batch version (fast)
        if batched:
            e = batch_error(net, training_batch)
            e.backward()
            training_error = e.item()

            with tr.no_grad():
                e = batch_error(net, testing_batch)
                testing_error = e.item()

        # take the next optimization step
        optimizer.step()    
        
        # print/save training progress
        if epoch % 1000 == 0:
            print("%d: %f, %f" % (epoch, training_error, testing_error))
        curves[0].append(training_error)
        curves[1].append(testing_error)
        
        
# visualize learning curves on train/test data
#pt.plot(curves[0], 'b-')
#pt.plot(curves[1], 'r-')
#pt.plot([0, len(curves[1])], [baseline_error, baseline_error], 'g-')
#pt.plot()
#pt.legend(["Train","Test","Baseline"])
#pt.show()

def nn_eval(state):
    with tr.no_grad():
        utility = net(encode(state).unsqueeze(0))
    return utility