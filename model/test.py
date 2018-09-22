from board import Board
from rook import Rook
from position import Position
from queen import Queen
from hill_climbing import *

init_position = Position(0, 0)
piece_1 = Rook(init_position, True)
piece_2 = Rook(init_position, True)
piece_3 = Rook(init_position, True)
piece_4 = Rook(init_position, True)
piece_5 = Rook(init_position, True)
piece_6 = Rook(init_position, True)
piece_7 = Rook(init_position, True)
piece_8 = Rook(init_position, True)
white_pieces = [piece_1, piece_2, piece_3,piece_4,piece_5,piece_6,piece_7,piece_8]
board = Board(8, white_pieces, [])
print(board.get_matrix())
board.draw()
print(board.count_all_conflict())
for piece in board.get_white_pieces():
    print(piece.get_position().get_x(), piece.get_position().get_y())
hill_climbing(board)
for piece in board.get_white_pieces():
    print(piece.get_position().get_x(), piece.get_position().get_y())
board.draw()
print(board.count_all_conflict())