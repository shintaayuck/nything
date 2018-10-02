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
    with open(fin,"r") as file_in:
        lines = file_in.read().splitlines()
        for line in lines :
            # print(line [-1:],end='-')
            if int(line[-1:]) > 0 :
                for idx in range(0,int(line[-1:])) :
                    if(line[-7:-2] == 'WHITE') :
                        # print("putih",end='-')
                        temp = line[:-8]
                        if(temp == 'BISHOP'):
                            # print("creating bishop")
                            white_pieces.append(Bishop(Position(),True))
                        elif(temp == 'KNIGHT'):
                            # print("creating knight")
                            white_pieces.append(Knight(Position(),True))
                        elif(temp == 'QUEEN'):
                            # print("creating QUEEN")
                            white_pieces.append(Queen(Position(),True))
                        elif(temp == 'ROOK'):
                            # print("creating ROOK")
                            white_pieces.append(Rook(Position(),True))

                    elif(line[-7:-2] == 'BLACK') :
                        # print("hitam",end='-')
                        temp = line[:-8]
                        if(temp == 'BISHOP'):
                            # print("creating bishop")
                            black_pieces.append(Bishop(Position(),False))
                        elif(temp == 'KNIGHT'):
                            # print("creating knight")
                            black_pieces.append(Knight(Position(),False))
                        elif(temp == 'QUEEN'):
                            # print("creating QUEEN")
                            black_pieces.append(Queen(Position(),False))
                        elif(temp == 'ROOK'):
                            # print("creating ROOK")
                            black_pieces.append(Rook(Position(),False))
        # print("--WHITE--")
        # print(white_pieces)
        # print()
        # print("--BLACK--")
        # print(black_pieces)
        # print()
    file_in.close()
    return white_pieces, black_pieces

def pickAlgorithm(white_pieces, black_pieces):
    board = Board(8, white_pieces, black_pieces)
    print("Algorithms:")
    print("1. Hill Climbing")
    print("2. Simulated Annealing")
    print("3. Genetic Algorithm")
    algo = int(input("Please enter your chosen algorithm (1 || 2 || 3) : "))
    if (algo == 1):
        result = climb_hill(board)
    elif (algo == 2):
        # schedule = float(input("Enter cooling schedule (e.g 0.99): "))
        result = simulated_annealing(board, 0.999, False)
    elif (algo == 3):
        population = initialize_population(white_pieces, black_pieces, 20)
        result = genetic_algorithm(population)
        print("Fitness: ", fitness(result))
    else:
        while (algo != 1 or algo != 2 or algo != 3):
            print("Wrong input!")
            algo = int(input("Please enter your chosen algorithm (1 || 2 || 3) : "))
            if (algo == 1):
                result = climb_hill(board)
            elif (algo == 2):
                schedule = float(input("Enter cooling schedule (e.g 0.99): "))
                result = simulated_annealing(board, schedule, False)
            elif (algo == 3):
                population = initialize_population(white_pieces, black_pieces, 20)
                result = genetic_algorithm(population)
                print("Fitness: ", fitness(result))

    return result

if __name__ == '__main__' :
    fin = input("Enter .txt file: ")
    white_pieces, black_pieces = parse(fin)
    # board = Board(8, white_pieces, black_pieces)
    result = pickAlgorithm(white_pieces, black_pieces)
    result.draw()
    again = input("Again? Answer with Y / N: ")
    while (again.lower() != 'n'):
        result = pickAlgorithm(white_pieces, black_pieces)
        result.draw()
        again = input("Again? Answer with Y / N: ")
