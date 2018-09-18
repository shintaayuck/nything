from position import Position


class Rook:
    
    #Constanta
    MAXSIZE = 8
    MINSIZE = 0

    def __init__(self):
        # nothing
        print("creating Rook")

    def possible_move_up(self, pos):
        li = []
        i = self.MINSIZE
        
        currentY = getattr(pos,'y') + 1
        for Y in range(currentY,self.MAXSIZE) :
            newPos = Position(getattr(pos,'x'),Y)
            li.append(newPos)
        return li

    
    def possible_move_right(self,pos):
        li = []
        i = self.MINSIZE

        currentX = getattr(pos,'x') + 1
        for X in range(currentX,self.MAXSIZE) :
            newPos = Position(X,getattr(pos,'y'))
            li.append(newPos)

        return li    

    def possible_move_down(self, pos):
        li = []
        i = self.MINSIZE

        currentY = getattr(pos,'y') - 1
        for Y in range(currentY,self.MINSIZE-1,-1) :
            newPos = Position(getattr(pos,'x'),Y)
            li.append(newPos)

        return li


    def possible_move_left(self,pos):
        li = []
        i = self.MINSIZE

        currentX = getattr(pos,'x') - 1
        for X in range(currentX,self.MINSIZE-1,-1) :
            newPos = Position(X,getattr(pos,'y'))
            li.append(newPos)

        return li

    def show_possible_move(self,pos):
        liOfAllPossible = []

        liOfAllPossible.append(self.possible_move_up(pos))
        liOfAllPossible.append(self.possible_move_down(pos))
        liOfAllPossible.append(self.possible_move_right(pos))
        liOfAllPossible.append(self.possible_move_left(pos))

        return liOfAllPossible

# def main() :
#     rook = Rook()
#     pos = Position(4,5)

#     li = rook.possibleConflict(pos)

#     for x in li :
#         for y in x :
#             y.print_attribute()
#         print()    

# if __name__ == '__main__' :
#     main()