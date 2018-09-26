from bishop import Bishop
from knight import Knight
from position import Position
from queen import Queen
from rook import Rook

def main():
    white_pieces = []
    black_pieces = []
    with open("input.txt","r") as file_in:
        lines = file_in.read().splitlines();
        for line in lines :
            print(line [-1:],end='-')
            if int(line[-1:]) > 0 :
                for idx in range(0,int(line[-1:])) :
                    if(line[-7:-2] == 'WHITE') :
                        print("putih",end='-')
                        temp = line[:-8]
                        if(temp == 'BISHOP'):
                            print("creating bishop")
                            white_pieces.append(Bishop(Position(),True))
                        elif(temp == 'KNIGHT'):
                            print("creating knight")
                            white_pieces.append(Knight(Position(),True))
                        elif(temp == 'QUEEN'):
                            print("creating QUEEN")
                            white_pieces.append(Queen(Position(),True))
                        elif(temp == 'ROOK'):
                            print("creating ROOK")
                            white_pieces.append(Rook(Position(),True))

                    elif(line[-7:-2] == 'BLACK') :
                        print("hitam",end='-')
                        temp = line[:-8]
                        if(temp == 'BISHOP'):
                            print("creating bishop")
                            black_pieces.append(Bishop(Position(),False))
                        elif(temp == 'KNIGHT'):
                            print("creating knight")
                            black_pieces.append(Knight(Position(),False))
                        elif(temp == 'QUEEN'):
                            print("creating QUEEN")
                            black_pieces.append(Queen(Position(),False))
                        elif(temp == 'ROOK'):
                            print("creating ROOK")
                            black_pieces.append(Rook(Position(),False))
        print("--WHITE--")
        print(white_pieces)
        print()
        print("--BLACK--")
        print(black_pieces)

    file_in.close()


if __name__ == '__main__' :
    main()
