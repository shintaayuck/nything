import random

from board import Board

def genetic_algorithm(population, mutation_probability = 1.0):
    population.sort()

    # crossover
    new_population = []
    weight = [w[0] for w in population]
    for _ in range(len(population)):
        # idx_parent1 = 
        pass

    if random.random() <= mutation_probability:
        # mutasi
        pass

    # return population


def initialize_population(pieces, initial_population = 10):
    white_pieces = []
    black_pieces = []
    population = []

    for piece in pieces:
        if piece.color:
            white_pieces.append(piece)
        else:
            black_pieces.append(piece)
    
    for _ in range(0,10):
        board = Board(8, white_pieces, black_pieces)
        population.append((fitness(board), board))
    
    return population


def fitness(board):
    return (board.enemy_conflict - board.ally_conflict)


def crossover(board1, board2):
    board1_piece = board1.white_pieces.append(board1.black_pieces)
    board2_piece = board2.white_pieces.append(board2.black_pieces)

    piece_count = len(board1_piece)
    crossover_index = random.randint(1, piece_count - 1)

    for n in range(crossover_index, piece_count):
        board1_piece[n].position, board2_piece[n].position \
            = board2_piece[n].position, board1_piece[n].position
    
    n_white = len(board1.white_pieces)
    n_black = len(board1.black_pieces)

    board1.white_pieces = board1_piece[:n_white]
    board1.black_pieces = board1_piece[-n_black:]

    board2.white_pieces = board2_piece[:n_white]
    board2.black_pieces = board2_piece[-n_black:]

    return board1, board2