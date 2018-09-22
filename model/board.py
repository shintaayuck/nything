import random
import time
import copy
from position import Position
from bishop import Bishop
from rook import Rook
from queen import Queen
from knight import Knight

class Board :
	'Chess board for solving n-ything problem'
	#constructor
	def __init__(self, size = None, white_pieces = None, black_pieces = None) :
		random.seed(time.time())
		self.__size = size if size is not None else 8
		self.__matrix = []
		self.__white_pieces = white_pieces if white_pieces is not None else []
		self.__black_pieces = black_pieces if black_pieces is not None else []
		self.__matrix = [[None for i in range(self.__size)] for j in range(self.__size)]
		self.__ally_conflict = 0
		self.__enemy_conflict = 0
		for piece in white_pieces :
			occupied = True
			while occupied :
				x = random.randint(0,self.__size-1)
				y = random.randint(0,self.__size-1)
				if(self.__matrix[x][y] == None) :
					occupied = False
			self.__matrix[x][y] = piece
			piece.position = Position(x,y)
		for piece in black_pieces :
			occupied = True
			while occupied :
				x = random.randint(0,self.__size-1)
				y = random.randint(0,self.__size-1)
				if(self.__matrix[x][y] == None) :
					occupied = False
			self.__matrix[x][y] = piece
			piece.position = Position(x,y)

	#getters and setters
	@property
	def size(self) :
		return self.__size

	@property
	def matrix(self) :
		return self.__matrix

	@property
	def white_pieces(self) :
		return self.__white_pieces

	@property
	def black_pieces(self) :
		return self.__black_pieces

	@property
	def ally_conflict(self) :
		return self.__ally_conflict

	@property
	def enemy_conflict(self) :
		return self.__enemy_conflict

	@size.setter
	def size(self, size) :
		self.__size = size

	@matrix.setter
	def matrix(self, matrix) :
		self.__matrix = matrix

	@white_pieces.setter
	def white_pieces(self, white_pieces) :
		self.__white_pieces = copy.deepcopy(white_pieces)

	@black_pieces.setter
	def black_pieces(self, black_pieces) :
		self.__black_pieces = copy.deepcopy(black_pieces)

	@ally_conflict.setter
	def ally_conflict(self, ally_conflict) :
		self.__ally_conflict = ally_conflict

	@enemy_conflict.setter
	def enemy_conflict(self, enemy_conflict) :
		self.__enemy_conflict = enemy_conflict

	#method functions
	#delete a piece from specific position
	def delete_piece(self, position) :
		result = self.__matrix[position.x, position.y]
		self.__matrix[position.x, position.y] = None
		return result

	#insert a piece to specific position
	def insert_piece(self, position, piece) :
		self.__matrix[position.x, position.y] = piece

	#move a piece to specific position
	def move_piece(self, piece, goal) :
	    init_x = piece.position.x
	    init_y = piece.position.y
	    piece.position = goal
	    self.__matrix[init_x][init_y] = None
	    self.__matrix[goal.x][goal.y] = piece

	#count a piece's conflict
	def count_conflict(self, possible_moves, color) :
		result = [0,0]
		for moves in possible_moves :
			if(type(moves) == type(Position())) :
				if(self.__matrix[moves.x][moves.y] != None) :
					if(self.__matrix[moves.x][moves.y].color == color) :
						result[0] += 1
					else :
						result[1] += 1
					break
			else :
				for move in moves :
					if(self.__matrix[move.x][move.y] != None) :
						if(self.__matrix[move.x][move.y].color == color) :
							result[0] += 1
						else :
							result[1] += 1
						break
		return result


	#count all pieces' conflict
	def count_all_conflict(self) :
		self.__ally_conflict = 0
		self.__enemy_conflict = 0
		for piece in self.__white_pieces :
			possible_moves = piece.show_possible_moves(piece.position)
			piece_conflict = self.count_conflict(possible_moves, piece.color)
			self.__ally_conflict += piece_conflict[0]
			self.__enemy_conflict += piece_conflict[1]
		for piece in self.__black_pieces :
			possible_moves = piece.show_possible_moves(piece.position)
			piece_conflict = self.count_conflict(possible_moves, piece.color)
			self.__ally_conflict += piece_conflict[0]
			self.__enemy_conflict += piece_conflict[1]

	#draw
	def draw(self) :
		for i in range(self.__size) :
			for j in range(self.__size) :
				if self.__matrix[i][j] == None :
					print('- ', end='')
				else :
					queen = Queen()
					rook = Rook()
					bishop = Bishop()
					knight = Knight()
					if(type(self.__matrix[i][j]) == type(queen)) :
						if(self.__matrix[i][j].color == True) :
							print('Q ', end='')
						else :
							print('q ', end='')
					elif(type(self.__matrix[i][j]) == type(rook)) :
						if(self.__matrix[i][j].color == True) :
							print('R ', end='')
						else :
							print('r ', end='')
					elif(type(self.__matrix[i][j]) == type(bishop)) :
						if(self.__matrix[i][j].color == True) :
							print('B ', end='')
						else :
							print('b ', end='')
					elif(type(self.__matrix[i][j]) == type(knight)) :
						if(self.__matrix[i][j].color == True) :
							print('K ', end='')
						else :
							print('k ', end='')
			print('')
