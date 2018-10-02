import copy
import sys
import random
from position import Position
from board import Board
from bishop import Bishop
from rook import Rook
from queen import Queen
from knight import Knight

#count delta of x and y
def delta(x, y) :
    return y - x

#count the improvement from initial state to goal state
def count_improvement(board, piece, goal) :
    init_possible_moves = piece.show_possible_moves()
    goal_possible_moves = piece.show_possible_moves(goal)
    init_conflict = board.count_conflict(init_possible_moves, piece.color)
    goal_conflict = board.count_conflict(goal_possible_moves, piece.color)
    delta_init = delta(init_conflict[0], init_conflict[1])
    delta_goal = delta(goal_conflict[0], goal_conflict[1])
    return delta(delta_init, delta_goal)

#find optimal neighbor
#return the piece and its goal position with how much it improves
def find_optimal_neighbor(board) :
    best_improvement = -sys.maxsize - 1
    all_pieces = board.combine_pieces()
    for piece in all_pieces :
        x = piece.position.x
        y = piece.position.y
        board.matrix[x][y] = None
        for i in range(board.size):
            for j in range(board.size):
                if(board.matrix[i][j] == None) :
                    improvement = count_improvement(board, piece, Position(i,j))
                    if(improvement > best_improvement):
                        best_improvement = improvement
                        goal = Position(i,j)
                        best_piece = piece
        board.matrix[x][y] = piece
    return (best_piece, goal, best_improvement)

#do hill climbing algorithm
def climb_hill(board) :
    n = 0
    climb = True
    while(n < 50 and climb) :
        board.count_all_conflict()
        optimal_neighbor = find_optimal_neighbor(board)
        optimal_piece = optimal_neighbor[0]
        optimal_goal = optimal_neighbor[1]
        improvement = optimal_neighbor[2]
        if(improvement == 0) :
            climb = False
        else :
            board.move_piece(optimal_piece, optimal_goal)
        n += 1
    # board.draw()
    print('Ally conflict :', board.ally_conflict)
    print('Enemy conflict :', board.enemy_conflict)
    print('Score :', delta(board.ally_conflict, board.enemy_conflict))
    print('')
    print('Number of iteration :', n)
    return board

# def main() :
#     init_position = Position(0, 0)
#     piece_1 =Bishop(init_position, True)
#     piece_2 = Bishop(init_position, True)
#     # piece_6 = Rook(init_position, True)
#     # piece_7 = Bishop(init_position, True)
#     # piece_8 = Knight(init_position, True)
#     white_pieces = [piece_1, piece_2]
#     # black_pieces = [piece_3, piece_4, piece_5]
#     # , piece_3,piece_4]
#     # ,piece_5,piece_6,piece_7,piece_8]
#     black_pieces = copy.deepcopy(white_pieces)
#     for piece in black_pieces :
#         piece.color = False
#     board = Board(8, white_pieces, black_pieces)
#     climb_hill(board)

# main()
