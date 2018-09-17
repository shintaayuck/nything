from Position import *


class Rook:

    def __init__(self):
        # nothing
        print("creating Rook")

    def possibleConflictUp(self, pos):
        li = []
        i = 1
        po = Position()
        currentY = getattr(pos,'y') + 1
        print("currentPos : "+pos.getCordinate()+" goto up")
        for Y in range(currentY,9) :
            newPos1 = Position(getattr(pos,'x'),Y)
            li.append(newPos1)
        for p in li :
            p.printAtribute()
        return li
    
    def possibleConflictRight(self,pos):
        li = []
        i = 1
        po = Position()
        currentX = getattr(pos,'x') + 1
        print("currentPos : "+pos.getCordinate()+" goto right")
        for X in range(currentX,9) :
            newPos1 = Position(X,getattr(pos,'y'))
            li.append(newPos1)
        for p in li :
            p.printAtribute()
        return li    

    def possibleConflictDown(self, pos):
        li = []
        i = 1
        po = Position()
        currentY = getattr(pos,'y') + 1
        print("currentPos : "+pos.getCordinate()+ " goto down")
        for Y in range(currentY,0,-1) :
            newPos1 = Position(getattr(pos,'x'),Y)
            li.append(newPos1)
        for p in li :
            p.printAtribute()
        return li


    def possibleConflictLeft(self,pos):
        li = []
        i = 1
        po = Position()
        currentX = getattr(pos,'x') + 1
        print("currentPos : "+pos.getCordinate()+" goto left")
        for X in range(currentX,0,-1) :
            newPos1 = Position(X,getattr(pos,'y'))
            li.append(newPos1)
        for p in li :
            p.printAtribute()
        return li

    # def possibleConflict(self,pos):
    #     liOfAllPossible = []
    #     liPossible = []
    #     liPossible = possibleConflictUp(pos)
    #     liOfAllPossible.append(liPossible)
    #     print()
    #     liOfAllPossible.append(possibleConlictDown(pos))
    #     print()
    #     liOfAllPossible.append(possibleConlictRight(pos))
    #     print()
    #     liOfAllPossible.append(possibleConlictLeft(pos))

    #     return liOfAllPossible

def main() :
    rook = Rook()
    pos = Position(4,5)

    rook.possibleConflict(pos)
    

if __name__ == '__main__' :
    main()