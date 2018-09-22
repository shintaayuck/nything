from board import Board
# from knight import Knight
from position import Position
from queen import Queen
from rook import Rook

import decimal
import math
import random
import copy

def simulated_annealing(board,schedule):
    solution = False
    temperature = 2000
    current_board = board
    current_state = board.white_pieces
    second_board = copy.deepcopy(board)
    li = second_board.white_pieces
    second_board.reset_board_matrix()

    current_board.draw()
    print()
    li[0].position.x = 0
    li[0].position.y = 0
    second_board.move_all_piece()
    second_board.draw()
    # for piece in current_state :
    #     piece.get_position().print_attribute()
    # current_board.draw()
    # current_board.set_white_pieces(current_state)
    # current_board.move_all_piece()

    print(eval(board))
    print("\n\n")




    # for t in range(0,2) :
    #     second_board = Board(8,[],[])
    #     temperature *= schedule
    #     second_state = current_state[:]
    #     second_state,second_board = random_move_set(second_state,second_board)

    #     delta_e = eval(current_state,current_board) - eval(second_state,second_board)
    #     print(eval(current_state,current_board),"-",eval(second_state,second_board))

    #     current_board.set_white_pieces(current_state)
    #     current_board.draw()
    #     print("\n\n")
    #     # exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-dw) * decimal.Decimal(temperature)))


def eval(board):
    board.count_all_conflict()
    return board.ally_conflict




def main():
    li = []
    for i in range (0,8):
        rook = Rook()
        li.append(rook)
    board = Board(8,li,[])
    # print(li)
    print("panjang li",len(li))
    simulated_annealing(board,0.99)

if __name__ == '__main__' :
    main()