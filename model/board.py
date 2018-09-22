import random
import time
import copy
from position import Position
from bishop import Bishop
from rook import Rook
from queen import Queen

class Board :
	'Chess board for solving n-ything problem'
	#constructor
	def __init__(self, size = None, white_pieces = None, black_pieces = None) :
		random.seed(time.time())
		self.size = size if size is not None else 8
		self.matrix = []
		self.white_pieces = white_pieces if white_pieces is not None else []
		self.black_pieces = black_pieces if black_pieces is not None else []
		self.matrix = [[None for i in range(self.size)] for j in range(self.size)]
		self.ally_conflict = 0
		self.enemy_conflict = 0
		for piece in white_pieces :
			occupied = True
			while occupied :
				x = random.randint(0,self.size-1)
				y = random.randint(0,self.size-1)
				if(self.matrix[x][y] == None) :
					occupied = False
			self.matrix[x][y] = piece
			piece.set_position(Position(x,y))
		for piece in black_pieces :
			occupied = True
			while occupied :
				x = random.randint(0,self.size-1)
				y = random.randint(0,self.size-1)
				if(self.matrix[x][y] == None) :
					occupied = False
			self.matrix[x][y] = piece
			piece.set_position(Position(x,y))

	def __str__(self):
		return str(self.__dict__)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	#getters and setters
	def get_size(self) :
		return self.size

	def get_matrix(self) :
		return self.matrix

	def get_white_pieces(self) :
		return self.white_pieces

	def get_black_pieces(self) :
		return self.black_pieces

	def get_ally_conflict(self) :
		return self.ally_conflict

	def get_enemy_conflict(self) :
		return self.enemy_conflict

	def set_size(self, size) :
		self.size = size

	def set_matrix(self, matrix) :
		self.matrix = matrix

	def set_white_pieces(self, white_pieces) :
		self.white_pieces = copy.deepcopy(white_pieces)

	def set_black_pieces(self, black_pieces) :
		self.black_pieces = copy.deepcopy(black_pieces)

	def set_ally_conflict(self, ally_conflict) :
		self.ally_conflict = ally_conflict

	def set_enemy_conflict(self, enemy_conflict) :
		self.enemy_conflict = enemy_conflict

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
	def count_conflict(self, possible_moves, color) :
		result = [0,0]
		for moves in possible_moves :
			for move in moves :
				if(self.matrix[move.get_x()][move.get_y()] != None) :
					if(self.matrix[move.get_x()][move.get_y()].get_color() == color) :
						result[0] += 1
					else :
						result[1] += 1
					break
		return result


	#count all pieces' conflict
	def count_all_conflict(self) :
		self.ally_conflict = 0
		self.enemy_conflict = 0
		for piece in self.white_pieces :
			possible_moves = piece.show_possible_moves(piece.get_position())
			piece_conflict = self.count_conflict(possible_moves, piece.get_color())
			self.ally_conflict += piece_conflict[0]
			self.enemy_conflict += piece_conflict[1]
		for piece in self.black_pieces :
			possible_moves = piece.show_possible_moves(piece.get_position())
			piece_conflict = self.count_conflict(possible_moves, piece.get_color())
			self.ally_conflict += piece_conflict[0]
			self.enemy_conflict += piece_conflict[1]

	#draw
	def draw(self) :
		for i in range(self.size) :
			for j in range(self.size) :
				if self.matrix[i][j] == None :
					print('- ', end='')
				else :
					queen = Queen()
					rook = Rook()
					bishop = Bishop()
					if(type(self.matrix[i][j]) == type(queen)) :
						if(self.matrix[i][j].get_color() == True) :
							print('Q ', end='')
						else :
							print('q ', end='')
					elif(type(self.matrix[i][j]) == type(rook)) :
						if(self.matrix[i][j].get_color() == True) :
							print('R ', end='')
						else :
							print('r ', end='')
					elif(type(self.matrix[i][j]) == type(bishop)) :
						if(self.matrix[i][j].get_color() == True) :
							print('B ', end='')
						else :
							print('b ', end='')
			print('')

	def move_piece(self, piece, goal) :
	    init_x = piece.get_position().get_x()
	    init_y = piece.get_position().get_y()
	    piece.set_position(goal)
	    self.matrix[init_x][init_y] = None
	    self.matrix[goal.get_x()][goal.get_y()] = piece
