from bishop import Bishop
from knight import Knight
from position import Position
from queen import Queen
from rook import Rook
from hill_climbing import *
from simulated_annealing import *
from ga import *


def parse(fin):
    white_pieces = []
    black_pieces = []
    with open(fin, "r") as file_in:
        lines = file_in.read().splitlines()
        for line in lines:
            if int(line[-1:]) > 0:
                for idx in range(0, int(line[-1:])):
                    if(line[-7:-2] == 'WHITE'):
                        temp = line[:-8]
                        if(temp == 'BISHOP'):
                            white_pieces.append(Bishop(Position(), True))
                        elif(temp == 'KNIGHT'):
                            white_pieces.append(Knight(Position(), True))
                        elif(temp == 'QUEEN'):
                            white_pieces.append(Queen(Position(), True))
                        elif(temp == 'ROOK'):
                            white_pieces.append(Rook(Position(), True))

                    elif(line[-7:-2] == 'BLACK'):
                        temp = line[:-8]
                        if(temp == 'BISHOP'):
                            black_pieces.append(Bishop(Position(), False))
                        elif(temp == 'KNIGHT'):
                            black_pieces.append(Knight(Position(), False))
                        elif(temp == 'QUEEN'):
                            black_pieces.append(Queen(Position(), False))
                        elif(temp == 'ROOK'):
                            black_pieces.append(Rook(Position(), False))

    file_in.close()
    return white_pieces, black_pieces


def pickAlgorithm(white_pieces, black_pieces):
    board = Board(8, white_pieces, black_pieces)
    print("Algorithms:")
    print("1. Hill Climbing")
    print("2. Simulated Annealing")
    print("3. Genetic Algorithm")
    algo = int(input("Please enter your chosen algorithm (1 || 2 || 3): "))
    if (algo == 1):
        result = climb_hill(board)
    elif (algo == 2):
        result = simulated_annealing(board, 0.999, False)
    elif (algo == 3):
        population = initialize_population(white_pieces, black_pieces, 20)
        result = genetic_algorithm(population)
        result.count_all_conflict()
        print("Ally conflict: ", result.ally_conflict)
        print("Enemy conflict: ", result.enemy_conflict)
        print("Score: ", fitness(result))
    else:
        while (algo != 1 or algo != 2 or algo != 3):
            print("Wrong input!")
            algo = int(
                input("Please enter your chosen algorithm (1 || 2 || 3): "))
            if (algo == 1):
                result = climb_hill(board)
            elif (algo == 2):
                schedule = float(
                    input("Enter cooling schedule (e.g 0.99): "))
                result = simulated_annealing(board, schedule, False)
            elif (algo == 3):
                population = initialize_population(white_pieces,
                                                   black_pieces, 20)
                result = genetic_algorithm(population)
                result.count_all_conflict()
                print("Ally conflict: ", result.ally_conflict)
                print("Enemy conflict: ", result.enemy_conflict)
                print("Score: ", fitness(result))

    return result


if __name__ == '__main__':
    fin = input("Enter .txt file: ")
    white_pieces, black_pieces = parse(fin)
    result = pickAlgorithm(white_pieces, black_pieces)
    result.draw()
    print(result.ally_conflict, " ", result.enemy_conflict)
    again = input("Again? Answer with Y / N: ")
    while (again.lower() != 'n'):
        result = pickAlgorithm(white_pieces, black_pieces)
        result.draw()
        print(result.ally_conflict, " ", result.enemy_conflict)
        again = input("Again? Answer with Y / N: ")
