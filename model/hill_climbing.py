import copy
import sys
from board import Board
from position import Position

def delta(x, y) :
    return y - x


# def find_better_board(board) :
#     result = copy.deepcopy(board)
#     for piece in result.get_white_pieces():
#         x = piece.get_position().get_x()
#         y = piece.get_position().get_y()
#         result.get_matrix()[x][y] = None
#         init_conflict = result.count_conflict(piece.show_possible_moves())
#         if(init_conflict == 0):
#             result.get_matrix()[x][y] = piece
#             piece.set_position(Position(x,y))
#         else:
#             goal_conflict = sys.maxsize
#             goal = Position(x,y)
#             for i in range(result.get_size()):
#                 for j in range(result.get_size()):
#                     if(result.get_matrix()[i][j] == None):
#                         possible_moves = piece.show_possible_moves(Position(i,j))
#                         temp_conflict = result.count_conflict(possible_moves)
#                         if(temp_conflict < goal_conflict):
#                             goal_conflict = temp_conflict
#                             goal.set_x(i)
#                             goal.set_y(j)
#             result.get_matrix()[goal.get_x()][goal.get_y()] = piece
#             piece.set_position(Position(goal.get_x(), goal.get_y()))
#     return result

# def find_worst_piece(board) :
#     min_delta_conflict = sys.maxsize
#     for piece in board.get_white_pieces() :
#         x = piece.get_position().get_x()
#         y = piece.get_position().get_y()
#         temp_conflict = result.count_conflict(piece.show_possible_moves(), piece.get_color())
#         delta_temp_conflict = temp_conflict[1] - temp_conflict[0]
#         if(delta_temp_conflict < min_delta_conflict) :
#             min_delta_conflict = delta_temp_conflict
#             result = piece
#     for piece in board.get_black_pieces() :
#         x = piece.get_position().get_x()
#         y = piece.get_position().get_y()
#         temp_conflict = result.count_conflict(piece.show_possible_moves(), piece.get_color())
#         delta_temp_conflict = temp_conflict[1] - temp_conflict[0]
#         if(delta_temp_conflict < min_delta_conflict) :
#             min_delta_conflict = delta_temp_conflict
#             result = piece
#     return piece

def find_optimal_neighbor(board) :
    best_improvement = -sys.maxsize - 1
    for piece in board.white_pieces :
        x = piece.position.x
        y = piece.position.y
        board.matrix[x][y] = None
        for i in range(board.size):
            for j in range(board.size):
                if(board.matrix[i][j] == None) :
                    init_possible_moves = piece.show_possible_moves()
                    possible_moves = piece.show_possible_moves(Position(i,j))
                    init_conflict = board.count_conflict(init_possible_moves, piece.color)
                    delta_init = delta(init_conflict[0], init_conflict[1])
                    temp_conflict = board.count_conflict(possible_moves, piece.color)
                    delta_temp = delta(temp_conflict[0], temp_conflict[1])
                    improvement = delta(delta_init, delta_temp)
                    if(improvement > best_improvement):
                        best_improvement = improvement
                        goal = Position(i,j)
                        best_piece = piece
        board.matrix[x][y] = piece
    return (best_piece, goal, best_improvement)


def climb_hill(board) :
    n = 0
    climb = True
    while(n < 20 and climb) :
        board.draw()
        board.count_all_conflict()
        print('Ally conflict :', board.ally_conflict)
        print('Enemy conflict :', board.enemy_conflict)
        print('Score :', delta(board.ally_conflict, board.enemy_conflict))
        print('')
        optimal_neighbor = find_optimal_neighbor(board)
        optimal_piece = optimal_neighbor[0]
        optimal_goal = optimal_neighbor[1]
        improvement = optimal_neighbor[2]
        if(improvement == 0) :
            climb = False
        else :
            board.move_piece(optimal_piece, optimal_goal)
        n += 1
    print('Number of iteration :', n)




# def hill_climbing(board):
#     n = 0
#     climb = True
#     while(n < 20 and climb) :
#         board.draw()
#         print(board.count_all_conflict())
#         print('')
#         if(board.count_all_conflict() == 0) :
#             climb = False
#         else :
#             neighbor = find_better_board(board)
#             if(neighbor.count_all_conflict() < board.count_all_conflict()) :
#                 board = neighbour
#             else :
#                 climb = False
#         n += 1
#     print('Number of iteration :', n)
