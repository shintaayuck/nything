from board import Board
# from knight import Knight
from position import Position
from queen import Queen
from rook import Rook

import decimal
import math
import random
import copy

def simulated_annealing(board,schedule,is_one_color,number_step):
    solution = False
    temperature = 4000
    current_board = copy.deepcopy(board)

    for t in range (0, number_step):
        second_board = copy.deepcopy(board)
        li_pieces = second_board.combine_pieces()

        idx = random.randint(0,len(second_board.combine_pieces())-1)
        if (temperature > 0.02):
            temperature *= schedule
        
        temp_pos = second_board.random_position()
        second_board.move_piece(li_pieces[idx],temp_pos)

        delta_e = (eval(current_board) - eval(second_board))
        

        if (delta_e >= 0) :
            current_board = copy.deepcopy(second_board)
        else :
            prob = 1/(math.e ** (- delta_e /temperature ))
            if(prob > random.uniform(0,1)) :
                current_board = copy.deepcopy(second_board)
            print ("%d : %d - %.2f - temp: %.2f" % (t,delta_e,prob,temperature))
    
        if (is_one_color and current_board.ally_conflict == 0) :
            break
    
    print()
    print("Number of Ally Conflict : ",current_board.ally_conflict)
    print("Number of Enemy Conflict : ",current_board.enemy_conflict)
    print("Number of step : ",number_step)
    print("Score : ",current_board.enemy_conflict - current_board.ally_conflict)

    return current_board    

def eval(board):
    board.count_all_conflict()
    return board.ally_conflict
