import random
import time
from position import Position

class Board :
	'Chess board for solving n-ything problem'
	#constructor
	def __init__(self, size = None, white_pieces = None, black_pieces = None) :
		random.seed(time.time())
		self.size = size if size is not None else 8
		self.matrix = []
		self.white_pieces = []
		self.black_pieces = []
		columns = [None] * self.size
		for i in range(self.size) :
			self.matrix.append(columns)
		for piece in white_pieces :
			occupied = True
			while occupied :
				x = random.randint(0,self.size-1)
				y = random.randint(0,self.size-1)
				if(self.matrix[x][y] == None) :
					occupied = False
			self.matrix[x][y] = piece
		for piece in black_pieces :
			occupied = True
			while occupied :
				x = random.randint(0,self.size-1)
				y = random.randint(0,self.size-1)
				if(self.matrix[x][y] == None) :
					occupied = False
			self.matrix[x][y] = piece
	#getters and setters
	def get_size(self) :
		return self.size

	def get_matrix(self) :
		return self.matrix

	def get_white_pieces(self) :
		return self.white_pieces

	def get_black_pieces(self) :
		return self.black_pieces

	def set_size(self, size) :
		self.size = size

	def set_matrix(self, matrix) :
		self.matrix = matrix

	def set_white_pieces(self, white_pieces) :
		self.white_pieces = white_pieces

	def set_black_pieces(self, black_pieces) :
		self.black_pieces = black_pieces
	#method functions
	#delete a piece from specific position
	def delete_piece(self, position) :
		result = self.matrix[position.get_x(), position.get_y()]
		self.matrix[position.get_x(), position.get_y()] = None
		return result
	#insert a piece to specific position
	def insert_piece(self, position, piece) :
		self.matrix[position.get_x(), position.get_y()] = piece
	#move a piece to specific position
	def move_piece(self, init_position, goal_position) :
		piece = delete_piece(init_position)
		insert_piece(goal_position, piece)
	#count a piece's conflict
	def count_conflict(self, possible_moves) :
		result = 0
		for moves in possible_moves :
			for move in moves :
				if(self.matrix[move.get_x(), move.get_y()] != None) :
					result += 1
					break
		return result
	#count all pieces' conflict
	def count_all_conflict(self) :
		result = 0
		for piece in white_pieces :
			possible_moves = piece.show_possible_moves(piece.get_position().get_x(), piece.get_position().get_y())
			result += count_conflict(possible_moves)
		for piece in black_pieces :
			possible_moves = piece.show_possible_moves(piece.get_position().get_x(), piece.get_position().get_y())
			result += count_conflict(possible_moves)
		return result


	