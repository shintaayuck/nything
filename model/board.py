import random
import time
import copy
from position import Position
from bishop import Bishop
from rook import Rook
from queen import Queen
from knight import Knight


class Board:
    # 'Chess board for solving n-ything problem'
    # constructor
    def __init__(self, size=None, white_pieces=None, black_pieces=None):
        random.seed(time.time())
        self.__size = size if size is not None else 8
        self.__matrix = []
        self.__white_pieces = white_pieces if white_pieces is not None else []
        self.__black_pieces = black_pieces if black_pieces is not None else []
        self.__matrix = [[None for i in range(self.__size)] for j in
                         range(self.__size)]
        self.__ally_conflict = 0
        self.__enemy_conflict = 0
        all_pieces = self.combine_pieces()
        for piece in all_pieces:
            position = self.random_position()
            self.__matrix[position.x][position.y] = piece
            piece.position = position

    # getters and setters
    @property
    def size(self):
        return self.__size

    @property
    def matrix(self):
        return self.__matrix

    @property
    def white_pieces(self):
        return self.__white_pieces

    @property
    def black_pieces(self):
        return self.__black_pieces

    @property
    def ally_conflict(self):
        return self.__ally_conflict

    @property
    def enemy_conflict(self):
        return self.__enemy_conflict

    @size.setter
    def size(self, size):
        self.__size = size

    @matrix.setter
    def matrix(self, matrix):
        self.__matrix = matrix

    @white_pieces.setter
    def white_pieces(self, white_pieces):
        self.__white_pieces = copy.deepcopy(white_pieces)

    @black_pieces.setter
    def black_pieces(self, black_pieces):
        self.__black_pieces = copy.deepcopy(black_pieces)

    @ally_conflict.setter
    def ally_conflict(self, ally_conflict):
        self.__ally_conflict = ally_conflict

    @enemy_conflict.setter
    def enemy_conflict(self, enemy_conflict):
        self.__enemy_conflict = enemy_conflict

    def __lt__(self, other):
        return True

    def ___le__(self, other):
        return True

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True

    # method functions
    # delete a piece from specific position
    def delete_piece(self, position):
        result = self.__matrix[position.x, position.y]
        self.__matrix[position.x, position.y] = None
        return result

    # insert a piece to specific position
    def insert_piece(self, position, piece):
        self.__matrix[position.x, position.y] = piece

    # move a piece to specific position
    def move_piece(self, piece, goal):
        init_x = piece.position.x
        init_y = piece.position.y
        piece.position = goal
        self.__matrix[init_x][init_y] = None
        self.__matrix[goal.x][goal.y] = piece

    # combine pieces to one list
    def combine_pieces(self):
        result = []
        for piece in self.__white_pieces:
            result.append(piece)
        for piece in self.__black_pieces:
            result.append(piece)
        return result

    # return randomized unoccupied position
    def random_position(self):
        occupied = True
        while occupied:
            x = random.randint(0, self.__size-1)
            y = random.randint(0, self.__size-1)
            if(self.__matrix[x][y] is None):
                occupied = False
        return Position(x, y)

    # count a piece's conflict
    def count_conflict(self, possible_moves, color):
        result = [0, 0]
        for moves in possible_moves:
            if(type(moves) == type(Position())):
                if(self.__matrix[moves.x][moves.y] != None):
                    if(self.__matrix[moves.x][moves.y].color == color):
                        result[0] += 1
                    else:
                        result[1] += 1
                    break
            else:
                for move in moves:
                    if(self.__matrix[move.x][move.y] != None):
                        if(self.__matrix[move.x][move.y].color == color):
                            result[0] += 1
                        else:
                            result[1] += 1
                        break
        return result

    # count all pieces' conflict
    def count_all_conflict(self):
        self.__ally_conflict = 0
        self.__enemy_conflict = 0
        all_pieces = self.combine_pieces()
        for piece in all_pieces:
            possible_moves = piece.show_possible_moves(piece.position)
            piece_conflict = self.count_conflict(possible_moves, piece.color)
            self.__ally_conflict += piece_conflict[0]
            self.__enemy_conflict += piece_conflict[1]

    # draw
    def draw(self):
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__matrix[i][j] is None:
                    print('- ', end='')
                else:
                    self.__matrix[i][j].draw()
            print('')
