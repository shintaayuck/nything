from board import Board
from position import Position
import sys


def hill_climbing(board):
    for piece in board.get_white_pieces():
        x = piece.get_position().get_x()
        y = piece.get_position().get_y()
        board.get_matrix()[x][y]= None
        init_conflict = board.count_conflict(piece.show_possible_moves())
        if(init_conflict == 0):
            board.get_matrix()[x][y] = piece
        else:
            goal_conflict = sys.maxsize
            goal = Position(x,y)
            for i in range(board.get_size()):
                for j in range(board.get_size()):
                    if(board.get_matrix()[i][j] == None):
                        possible_moves = piece.show_possible_moves(Position(i,j))
                        temp_conflict = board.count_conflict(possible_moves)
                        if(temp_conflict < goal_conflict):
                            goal_conflict = temp_conflict
                            goal.set_x(i)
                            goal.set_y(j)
            board.get_matrix()[goal.get_x()][goal.get_y()] = piece
            piece.set_position(Position(goal.get_x(), goal.get_y()))

