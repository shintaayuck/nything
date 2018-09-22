from board import Board
# from knight import Knight
from position import Position
from queen import Queen
from rook import Rook

import decimal
import math
import random

def simulated_annealing(board,schedule):
    solution = False
    temperature = 2000
    current_board = Board(board.get_size(),board.get_white_pieces(),[])
    current_state = board.get_white_pieces()

    for t in range(0,2) :
        second_board = Board(8,[],[])
        temperature *= schedule
        second_state = []
        for i in range(0,len(current_state)):
            second_state.append(current_state[i])
        second_state,second_board = random_move_set(second_state,second_board)

        delta_e = eval(current_state,current_board) - eval(second_state,second_board)
        print(eval(current_state,current_board),"-",eval(second_state,second_board))

        current_board.set_white_pieces(current_state)
        current_board.draw()
        print("\n\n")
        # exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-dw) * decimal.Decimal(temperature)))


def eval(pieces,board):
    return board.count_all_conflict_white(pieces)

def random_move_set(pieces,board): 
    for piece in pieces :
        occupied = True
        while occupied :
            x = random.randint(0,board.get_size()-1)
            y = random.randint(0,board.get_size()-1)
            if(board.matrix[x][y] == None) :
                occupied = False
        board.matrix[x][y] = piece
        piece.set_position(Position(x,y))
    return pieces,board

def main():
    rook = Rook()
    print(rook.get_color())
    li = []
    for i in range (0,8):
        li.append(rook)
    board = Board(8,li,[])
    print(li)
    simulated_annealing(board,0.99)

if __name__ == '__main__' :
    main()