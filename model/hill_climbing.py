import copy
import sys
from board import Board
from position import Position

#count delta of x and y
def delta(x, y) :
    return y - x

#count the improvement from initial state to goal state
def count_improvement(init_conflict, current_conflict) :
    delta_init = delta(init_conflict[0], init_conflict[1])
    delta_current = delta(current_conflict[0], current_conflict[1])
    return delta(delta_init, delta_current)

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
                    init_possible_moves = piece.show_possible_moves()
                    possible_moves = piece.show_possible_moves(Position(i,j))
                    init_conflict = board.count_conflict(init_possible_moves, piece.color)
                    temp_conflict = board.count_conflict(possible_moves, piece.color)
                    improvement = count_improvement(init_conflict, temp_conflict)
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
    board.draw()    
    print('Ally conflict :', board.ally_conflict)
    print('Enemy conflict :', board.enemy_conflict)
    print('Score :', delta(board.ally_conflict, board.enemy_conflict))
    print('')
    print('Number of iteration :', n)
