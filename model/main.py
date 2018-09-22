import copy
from position import Position
from board import Board
from bishop import Bishop
from rook import Rook
from queen import Queen
from hill_climbing import *

init_position = Position(0, 0)
piece_1 = Rook(init_position, True)
piece_2 = Rook(init_position, True)
piece_3 = Bishop(init_position, True)
piece_4 = Rook(init_position, True)
piece_5 = Rook(init_position, True)
piece_6 = Rook(init_position, True)
piece_7 = Bishop(init_position, True)
piece_8 = Rook(init_position, True)
white_pieces = [piece_1, piece_2, piece_3,piece_4,piece_5,piece_6,piece_7,piece_8]
black_pieces = copy.deepcopy(white_pieces)
for piece in black_pieces :
	piece.color = False
board = Board(8, white_pieces, black_pieces)
climb_hill(board)
