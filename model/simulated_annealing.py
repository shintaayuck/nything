from board import Board
# from knight import Knight
from position import Position
from queen import Queen
from rook import Rook

import decimal
import math
import random
import copy

def simulated_annealing(board,schedule,is_one_color):
    solution = False
    temperature = 4000
    current_board = copy.deepcopy(board)

    current_board.draw()
    print(eval(current_board))
    print("Number of Ally Conflict : ",current_board.ally_conflict)
    print("Number of Enemy Conflict : ",current_board.enemy_conflict)

    for t in range (0, 500):
        second_board = copy.deepcopy(board)
        li_pieces = second_board.combine_pieces()

        idx = random.randint(0,len(second_board.combine_pieces())-1)
        # print(t,"-",idx,"-",t % 500)
        temperature *= schedule
        
        temp_pos = second_board.random_position()
        second_board.move_piece(li_pieces[idx],temp_pos)

        delta_e = (eval(current_board) - eval(second_board))
        prob = 1/(math.e ** (- t*delta_e /temperature ))

        # print ("%d - %.2f - temp: %.2f" % (delta_e,prob,temperature))
        if (delta_e > 0 or prob > random.uniform(0,1) ) :
            current_board = copy.deepcopy(second_board)
        # if(delta_e > 0) :
            # current_board = copy.deepcopy(second_board)

        if (is_one_color and current_board.ally_conflict == 0) :
            break
    
    print()
    current_board.draw()
    print("Number of Ally Conflict : ",current_board.ally_conflict)
    print("Number of Enemy Conflict : ",current_board.enemy_conflict)
    print("Number of step : ",t )
    print("Score : ",current_board.enemy_conflict - current_board.ally_conflict)

    return current_board    

def eval(board):
    board.count_all_conflict()
    return board.ally_conflict




def main():
    li = []
    li1 = []
    for i in range (0,8):
        rook = Rook()
        rook1 = Rook(Position(),False)
        li.append(rook)
        li1.append(rook1)
    
    board = Board(8,li,li1)
    # print(li)
    # print("panjang li",len(li))
    again= True
    while(again) :
        board = simulated_annealing(board,0.99,False)
        x = input("lagi ?")
        if(x == 'ga') :
            again = False

if __name__ == '__main__' :
    main()