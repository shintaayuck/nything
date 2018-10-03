from position import Position


class Rook:

    #Constanta
    MAXSIZE = 8
    MINSIZE = 0

    def __init__(self, pos = Position(), color = True):
        self.__possition = pos
        self.__color = color
    # getter attributes
    @property
    def position(self):
        return self.__position

    @property
    def color(self):
        return self.__color

    # setter attributes
    @position.setter
    def position(self, pos):
        self.__position = pos

    @color.setter
    def color(self, color):
        self.__color = color

    def possible_move_down(self, pos):
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

    def possible_move_up(self, pos):
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

    def show_possible_moves(self,position = None):
        liOfAllPossible = []
        pos = position if position is not None else self.position

        liOfAllPossible.append(self.possible_move_up(pos))
        liOfAllPossible.append(self.possible_move_down(pos))
        liOfAllPossible.append(self.possible_move_right(pos))
        liOfAllPossible.append(self.possible_move_left(pos))

        return liOfAllPossible

    def draw(self) :
        if (self.__color):
            print("R ",end = '')
        else:
            print("r ",end = '')
