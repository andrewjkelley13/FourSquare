import numpy as np
import matplotlib.pyplot as pt
import torch as tr

def state_string(state):
    return "\n".join(["".join(row) for row in state])

def det_player_type():
    player1_type = input("Player 1: Enter 0 for human control, Enter 1 for baseline AI, Enter 2 for Tree-Based:\n")
    player2_type = input("Player 2: Enter 0 for human control, Enter 1 for baseline AI, Enter 2 for Tree-Based:\n")
    return player1_type,player2_type

def det_board_size():
    boardsize = input("Enter 0 for a 5x6 board, Enter 1 for a 7x6 board, Enter 2 for a 9x6 board:\n")
    return boardsize

def score(state,boardsize):
    if boardsize == "0":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[5,1],state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[5,2],state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
        vert3 = state[5,3],state[4,3],state[3,3],state[2,3],state[1,3],state[0,3]
        vert4 = state[5,4],state[4,4],state[3,4],state[2,4],state[1,4],state[0,4]
        horiz0 = state[0,4],state[0,3],state[0,2],state[0,1],state[0,0]
        horiz1 = state[1,4],state[1,3],state[1,2],state[1,1],state[1,0]
        horiz2 = state[2,4],state[2,3],state[2,2],state[2,1],state[2,0]
        horiz3 = state[3,4],state[3,3],state[3,2],state[3,1],state[3,0]
        horiz4 = state[4,4],state[4,3],state[4,2],state[4,1],state[4,0]
        horiz5 = state[5,4],state[5,3],state[5,2],state[5,1],state[5,0]
        diag0 = state[5,0],state[4,1],state[3,2],state[2,3],state[1,4]
        diag1 = state[5,1],state[4,2],state[3,3],state[2,4]
        diag2 = state[4,0],state[3,1],state[2,2],state[1,3],state[0,4]
        diag3 = state[3,0],state[2,1],state[1,2],state[0,3]
        diagback0 = state[3,4],state[2,3],state[1,2],state[0,1]
        diagback1 = state[4,4],state[3,3],state[2,2],state[1,1],state[0,0]
        diagback2 = state[5,4],state[4,3],state[3,2],state[2,1],state[1,0]
        diagback3 = state[5,3],state[4,2],state[3,1],state[2,0]
    
    
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
            for h5 in range(len(horiz5)):
                if h5 < 2:
                    if (horiz5[h5] == horiz5[h5+1] == horiz5[h5+2] == horiz5[h5+3] == player): return value
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
            for d3 in range(len(diag3)):
                if d3 == 0:
                    if (diag3[d3] == diag3[d3+1] == diag3[d3+2] == diag3[d3+3] == player): return value
            for db0 in range(len(diagback0)):
                if db0 == 0:
                    if (diagback0[db0] == diagback0[db0+1] == diagback0[db0+2] == diagback0[db0+3] == player): return value
            for db1 in range(len(diagback1)):
                if db1 < 2:
                    if (diagback1[db1] == diagback1[db1+1] == diagback1[db1+2] == diagback1[db1+3] == player): return value
            for db2 in range(len(diagback2)):
                if db2 < 2:
                    if (diagback2[db2] == diagback2[db2+1] == diagback2[db2+2] == diagback2[db2+3] == player): return value
            for db3 in range(len(diagback3)):
                if db3 == 0:
                    if (diagback3[db3] == diagback3[db3+1] == diagback3[db3+2] == diagback3[db3+3] == player): return value
        return 0
    
    if boardsize == "1":
        vert0 = state[5,0],state[4,0],state[3,0],state[2,0],state[1,0],state[0,0]
        vert1 = state[5,1],state[4,1],state[3,1],state[2,1],state[1,1],state[0,1]
        vert2 = state[5,2],state[4,2],state[3,2],state[2,2],state[1,2],state[0,2]
        vert3 = state[5,3],state[4,3],state[3,3],state[2,3],state[1,3],state[0,3]
        vert4 = state[5,4],state[4,4],state[3,4],state[2,4],state[1,4],state[0,4]
        vert5 = state[5,5],state[4,5],state[3,5],state[2,5],state[1,5],state[0,5]
        vert6 = state[5,6],state[4,6],state[3,6],state[2,6],state[1,6],state[0,6]
        horiz0 = state[0,6],state[0,5],state[0,4],state[0,3],state[0,2],state[0,1],state[0,0]
        horiz1 = state[1,6],state[1,5],state[1,4],state[1,3],state[1,2],state[1,1],state[1,0]
        horiz2 = state[2,6],state[2,5],state[2,4],state[2,3],state[2,2],state[2,1],state[2,0]
        horiz3 = state[3,6],state[3,5],state[3,4],state[3,3],state[3,2],state[3,1],state[3,0]
        horiz4 = state[4,6],state[4,5],state[4,4],state[4,3],state[4,2],state[4,1],state[4,0]
        horiz5 = state[5,6],state[5,5],state[5,4],state[5,3],state[5,2],state[5,1],state[5,0]
        diag0 = state[5,0],state[4,1],state[3,2],state[2,3],state[1,4],state[0,5]
        diag1 = state[5,1],state[4,2],state[3,3],state[2,4],state[1,5],state[0,6]
        diag2 = state[5,2],state[4,3],state[3,4],state[2,5],state[1,6]
        diag3 = state[5,3],state[4,4],state[3,5],state[2,6]
        diag4 = state[4,0],state[3,1],state[2,2],state[1,3],state[4,0]
        diag5 = state[3,0],state[2,1],state[1,2],state[0,3]
        diagback0 = state[5,6],state[4,5],state[3,4],state[2,3],state[1,2],state[0,1]
        diagback1 = state[5,5],state[4,4],state[3,3],state[2,2],state[1,1],state[0,0]
        diagback2 = state[5,4],state[4,3],state[3,2],state[2,1],state[1,0]
        diagback3 = state[5,3],state[4,2],state[3,1],state[2,0]
        diagback4 = state[4,6],state[3,5],state[2,4],state[1,3],state[0,2]
        diagback5 = state[3,6],state[2,5],state[1,4],state[0,3]
    
    
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
            for h5 in range(len(horiz5)):
                if h5 < 4:
                    if (horiz5[h5] == horiz5[h5+1] == horiz5[h5+2] == horiz5[h5+3] == player): return value
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
                if d2 < 2:
                    if (diag2[d2] == diag2[d2+1] == diag2[d2+2] == diag2[d2+3] == player): return value
            for d3 in range(len(diag3)):
                if d3 == 0:
                    if (diag3[d3] == diag3[d3+1] == diag3[d3+2] == diag3[d3+3] == player): return value
            for d4 in range(len(diag3)):
                if d4 < 1:
                    if (diag4[d4] == diag4[d4+1] == diag4[d4+2] == diag4[d4+3] == player): return value
            for d5 in range(len(diag3)):
                if d5 == 0:
                    if (diag5[d5] == diag5[d5+1] == diag5[d5+2] == diag5[d5+3] == player): return value
            for db0 in range(len(diagback0)):
                if db0 < 3:
                    if (diagback0[db0] == diagback0[db0+1] == diagback0[db0+2] == diagback0[db0+3] == player): return value
            for db1 in range(len(diagback1)):
                if db1 < 3:
                    if (diagback1[db1] == diagback1[db1+1] == diagback1[db1+2] == diagback1[db1+3] == player): return value
            for db2 in range(len(diagback2)):
                if db2 < 2:
                    if (diagback2[db2] == diagback2[db2+1] == diagback2[db2+2] == diagback2[db2+3] == player): return value
            for db3 in range(len(diagback3)):
                if db3 == 0:
                    if (diagback3[db3] == diagback3[db3+1] == diagback3[db3+2] == diagback3[db3+3] == player): return value
            for db4 in range(len(diagback4)):
                if db4 < 1:
                    if (diagback4[db4] == diagback4[db4+1] == diagback4[db4+2] == diagback4[db4+3] == player): return value
            for db5 in range(len(diagback5)):
                if db5 == 0:
                    if (diagback5[db5] == diagback5[db5+1] == diagback5[db5+2] == diagback5[db5+3] == player): return value
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

def depth_limited_minimax(state, max_depth, evaluate):
    # returns chosen child state, utility
    player = get_player(state)
    children = children_of(state)
    value = score(state,boardsize)

    # base cases
    if len(children) == 0 or value != 0: return None, value
    if max_depth == 0: return None, evaluate(state)

    # recursive case
    results = [
        depth_limited_minimax(child, max_depth-1, evaluate)
        for child in children]

    _, utilities = zip(*results)
    if player == "X": action = np.argmax(utilities)
    if player == "O": action = np.argmin(utilities)
    return children[action], utilities[action]

def simple_evaluate(state):
    # count how many ways it is still possible to win or lose
    count = 0
    for player, value in (("X", 1), ("O", -1)):
        count += ((state == player) | (state == "_")).all(axis=0).sum() * value
        count += ((state == player) | (state == "_")).all(axis=1).sum() * value
        count += ((np.diag(state) == player) | (np.diag(state) == "_")).all() * value
        count += ((np.diag(np.rot90(state)) == player) | (np.diag(np.rot90(state)) == "_")).all() * value
    return count

if __name__ == "__main__":
    boardsize = det_board_size()
    if boardsize == "0":
        state = np.array([["_"]*5]*6)
        print(state)
    if boardsize == "1":
        state = np.array([["_"]*7]*6)
        print(state)
    if boardsize == "2":
        np.array([["_"]*9]*6)
    player1_type,player2_type = det_player_type()
    if (player1_type == "2"):
        state[5,3] = "X"
        
    max_depth = 5
    
    # Each player using minimax each turn to decide the next action and state
    while True:
      if len(children_of(state)) == 0 or score(state,boardsize) != 0: break

      print(state_string(state))
      #human as X vs human as O
      if (player1_type == "0") and (player2_type == "0"):
          if get_player(state) == "X":
            while True:
              row = int(input("Enter row: "))
              col = int(input("Enter col: "))
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                state[row,col] = "X"
                break
              print("Invalid choice.")
          if get_player(state) == "O":
            while True:
              row = int(input("Enter row: "))
              col = int(input("Enter col: "))
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "O"
                  break
              print("Invalid choice.")
      #human as X vs baseline AI as O
      if (player1_type == "0") and (player2_type == "1"):
          if get_player(state) == "X":
            while True:
              row = int(input("Enter row: "))
              col = int(input("Enter col: "))
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "X"
                  break
              print("Invalid choice.")
          if get_player(state) == "O":
            while True:
              row = np.random.randint(5)
              if boardsize == "0":
                  col = np.random.randint(4)
              if boardsize == "1":    
                  col = np.random.randint(6)
              if boardsize == "2":
                  col = np.random.randint(8)
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "O"
      #human as X vs tree search as O
      if (player1_type == "0") and (player2_type == "2"):
          if get_player(state) == "X":
            while True:
              row = int(input("Enter row: "))
              col = int(input("Enter col: "))
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "X"
                  break
              print("Invalid choice.")  
          if get_player(state) == "O":
            state, u = depth_limited_minimax(state, max_depth, simple_evaluate)
            print("evaluation:", u)
      #baseline AI as X vs human as O      
      if (player1_type == "1") and player2_type == "0":
          if get_player(state) == "X":
            while True:
              row = np.random.randint(5)
              if boardsize == "0":
                  col = np.random.randint(4)
              if boardsize == "1":    
                  col = np.random.randint(6)
              if boardsize == "2":
                  col = np.random.randint(8)
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "X"    
          if get_player(state) == "O":
            while True:
              row = int(input("Enter row: "))
              col = int(input("Enter col: "))
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "O"
                  break
              print("Invalid choice.")
      #baseline AI as X vs basline AI as O       
      if (player1_type == "1") and (player2_type == "1"):    
          if get_player(state) == "X":
            while True:
              row = np.random.randint(5)
              if boardsize == "0":
                  col = np.random.randint(4)
              if boardsize == "1":    
                  col = np.random.randint(6)
              if boardsize == "2":
                  col = np.random.randint(8)
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "X"     
          if get_player(state) == "O":
            while True:
              row = np.random.randint(5)
              if boardsize == "0":
                  col = np.random.randint(4)
              if boardsize == "1":    
                  col = np.random.randint(6)
              if boardsize == "2":
                  col = np.random.randint(8)
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "O"
      #tree search AI as X vs human as O            
      if (player1_type == "2") and (player2_type == "0"):
          if get_player(state) == "X":
            state, u = depth_limited_minimax(state, max_depth, simple_evaluate)
            print("evaluation:", u)
          if get_player(state) == "O":
            while True:
              row = int(input("Enter row: "))
              col = int(input("Enter col: "))
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "O"
                  break
              print("Invalid choice.")
      #tree search AI as X vs baseline AI as O        
      if (player1_type == "2") and (player2_type == "1"):
          if get_player(state) == "X":
            state, u = depth_limited_minimax(state, max_depth, simple_evaluate)
            print("evaluation:", u)
          if get_player(state) == "O":
            while True:
              row = np.random.randint(5)
              if boardsize == "0":
                  col = np.random.randint(4)
              if boardsize == "1":    
                  col = np.random.randint(6)
              if boardsize == "2":
                  col = np.random.randint(8)
              if (state[row,col] == "_") and ((row+1 == 6) or (state[row+1,col] == "X") or (state[row+1,col] == "O")):
                  state[row,col] = "O"
      #tree search AI as X vs tree search AI as O            
      if (player1_type == "2") and (player2_type == "2"):
          if get_player(state) == "X":
            state, u = depth_limited_minimax(state, max_depth, simple_evaluate)
            print("evaluation:", u)
          if get_player(state) == "O":
            state, u = depth_limited_minimax(state, max_depth, simple_evaluate)
            print("evaluation:", u)  
    print(state_string(state))
    print("Final score: ", score(state,boardsize))
    input("")        