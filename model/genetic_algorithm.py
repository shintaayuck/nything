import random
import math
import copy
import numpy as np
import time

from board import Board
from bishop import Bishop
from rook import Rook
from queen import Queen
from knight import Knight

def genetic_algorithm(population, mutation_probability = 1.0):
    population.sort(reverse=True)

    new_population = []

    # new_population = population[:math.ceil(len(population)/2)]
    print('old:\n{}'.format(population))

    for n in range(0, math.ceil(len(population)/2)):
        child_board_1, child_board_2 = crossover(population[n][1], population[(n+1)%len(population)][1])

    # min_score = min([w[0] for w in population])
    # if min_score < 0:
    #     weight = [w[0] - min_score for w in population]
    # else:
    #     weight = [w[0] for w in population]
    # total_weight = sum([w[0] for w in population])
    # weight = [w[0]/total_weight for w in population]
    # index = np.arange(len(population)) # for choosing parent by weight
    # for _ in range(math.floor(len(population)/2)):
    #     parent_board_indices = np.random.choice(index, 2, replace=True, p=weight)
    #     child_board_1, child_board_2 = crossover(population[parent_board_indices[0]][1], population[parent_board_indices[1]][1])

        if random.random() <= mutation_probability:
            child_board_1 = mutation(child_board_1)
        if random.random() <= mutation_probability:
            child_board_2 = mutation(child_board_2)

        new_population.append((fitness(child_board_1), child_board_1))
        new_population.append((fitness(child_board_2), child_board_2))
    
    new_population.sort(reverse=True)
    print('new:\n{}'.format(new_population))
    return new_population, new_population[0][1]


def initialize_population(pieces, initial_population = 10):
    white_pieces = []
    black_pieces = []
    population = []

    for piece in pieces:
        # new_piece = copy.deepcopy(piece)
        if piece.color:
            # white_pieces.append(new_piece)
            white_pieces.append(piece)
        else:
            # black_pieces.append(new_piece)
            black_pieces.append(piece)
    
    for _ in range(0,10):
        board = Board(8, white_pieces, black_pieces)
        population.append((fitness(board), board))
    
    return population


def fitness(board):
    board.count_all_conflict()
    return (board.enemy_conflict - board.ally_conflict)


def crossover(board1, board2):
    n_white = len(board1.white_pieces)
    n_black = len(board1.black_pieces)

    if n_white > 0:
        white_crossover_index = random.randint(1, n_white - 1)

        for n in range(white_crossover_index, n_white):
            board1.white_pieces[n], board2.white_pieces[n] = board2.white_pieces[n], board1.white_pieces[n]

    if n_black > 0:
        black_crossover_index = random.randint(1, n_black - 1)

        for n in range(black_crossover_index, n_black):
            board1.black_pieces[n], board2.black_pieces[n] = board2.black_pieces[n], board1.black_pieces[n]

    # board1_piece = board1.combine_pieces()
    # board2_piece = board2.combine_pieces()
    # piece_count = len(board1_white) + len(board1_black)
    # for n in range(crossover_index, piece_count):
    #     board1_piece[n].position, board2_piece[n].position \
    #         = board2_piece[n].position, board1_piece[n].position
    
    # n_white = len(board1.white_pieces)
    # n_black = len(board1.black_pieces)

    # board1.white_pieces = board1_piece[:n_white]
    # board1.black_pieces = board1_piece[-n_black:]

    # board2.white_pieces = board2_piece[:n_white]
    # board2.black_pieces = board2_piece[-n_black:]
    new_board1 = copy.deepcopy(board1)
    new_board2 = copy.deepcopy(board2)
    return new_board1, new_board2


def mutation(board):
    pieces = board.combine_pieces()
    piece_count = len(pieces)
    n_white = len(board.white_pieces)
    n_black = len(board.black_pieces)

    mutation_index = random.randint(0, piece_count-1)

    pieces[mutation_index].position.x = random.randint(0,7)
    pieces[mutation_index].position.y = random.randint(0,7)

    board.white_pieces = pieces[:n_white]
    board.black_pieces = pieces[-n_black:]

    return board


def convergent(max_scores, min_value):
    if np.std(max_scores) <= min_value:
        return True
    else:
        return False


if __name__ == '__main__':
    # input min value, initial population, mutation probability
    li = []
    max_scores = []
    for i in range (0,8):
        rook = Rook()
        li.append(rook)

    population = initialize_population(li, 10)

    # population = genetic_algorithm(population, 0.9)

    # while (len(max_scores) < 10) or not convergent(max_scores, 0.1):
    while (len(max_scores) < 10) or 0 not in max_scores:
        population, best_board = genetic_algorithm(population, 0.8)
        if len(max_scores) >= 10:
            max_scores.pop(0)
        max_scores.append(max(population)[0])
        print('max_scores:{}'.format(max_scores))
        print('====================')

    best_board.reset_board_matrix()
    best_board.move_all_piece()
    print(best_board)
    rooks = best_board.white_pieces
    print(li)
    print(rooks)
    for rook in rooks:
        print('({},{})'.format(rook.position.x, rook.position.y))
    best_board.draw()