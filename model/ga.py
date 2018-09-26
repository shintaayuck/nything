import random
import math
import copy
import numpy as np

from board import Board
from bishop import Bishop
from rook import Rook
from queen import Queen
from knight import Knight

def genetic_algorithm(population):
    # Precondition : population = initialize_population(white_pieces, black_pieces, 10)

    # sort population from the highest fitness
    sorted(population, reverse = True)

    # check for 100 times
    for iterate in range(100) :
        new_population = []

        for i in range(len(population)//2) :
            # selection
            pieces1 = population[i][1].combine_pieces()
            pieces2 = population[i+1][1].combine_pieces()

            # crossover
            pieces1 , pieces2 = crossover(pieces1, pieces2)

            # mutation
            # pieces1 = mutation(pieces1)
            # pieces2 = mutation(pieces2)

            board1 = Board()
            update_board(board1, pieces1)
            new_population.append((fitness(board1),board1))
            board2 = Board()
            update_board(board2, pieces2)
            new_population.append((fitness(board2),board2))
        population = copy.deepcopy(new_population)
        sorted(population,reverse = True)

    return population[0][1]

# randomize population that consists of n boards
def initialize_population(white_pieces, black_pieces, n_boards) :
    population = []

    for n in range(n_boards) :
        new_white_pieces = copy.deepcopy(white_pieces)
        new_black_pieces = copy.deepcopy(black_pieces)

        # randomize positions
        new_board = Board(8, new_white_pieces, new_black_pieces)
        population.append((fitness(new_board), new_board))

    return population

# crossover parents
def crossover(board1_pieces, board2_pieces) : #list of pieces

    # randomize cutting point
    cutting_point = random.randint(0, len(board1_pieces)-1)

    # swap position
    for i in range(cutting_point) :
        temp_piece = copy.deepcopy(board1_pieces[i])
        board1_pieces[i] = copy.deepcopy(board2_pieces[i])
        board2_pieces[i] = copy.deepcopy(temp_piece)

    # new board pieces
    return board1_pieces, board2_pieces

# mutate a piece's position
def mutation(board_pieces) :

    board_pieces[random.randint(0,len(board_pieces)-1)].position.x = random.randint(0,7)
    board_pieces[random.randint(0,len(board_pieces)-1)].position.y = random.randint(0,7)

    return board_pieces

def update_board(board, pieces) :
    board.white_pieces = []
    board.black_pieces = []
    board.matrix = [[None for i in range(board.size)] for j in range(board.size)]

    for piece in pieces :
        board.matrix[piece.position.x][piece.position.y] = piece
        if piece.color :
            board.white_pieces.append(piece)

        else :
            board.black_pieces.append(piece)

    return board

def fitness(board):
    board.count_all_conflict()
    return (board.enemy_conflict - board.ally_conflict)

if __name__ == '__main__':
    white = []
    white.append(Queen())
    white.append(Rook())
    white.append(Bishop())
    white.append(Knight())

    black = []
    black.append(Queen())
    black.append(Rook())
    black.append(Bishop())
    black.append(Knight())
    for b in black :
        b.color = False

    population = initialize_population(white, black, 20)


    result = genetic_algorithm(population)
    print(result, "yeay")
    result.draw()

    print(fitness(result))
