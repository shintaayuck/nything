from position import Position


class Bishop:

    # constants
    MAXSIZE = 8
    MINSIZE = 0

    # constructor
    def __init__(self, pos=Position(), color=True):
        self.__position = pos
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

    # methods
    def possible_move_up_left(self, pos):
        # this method calculates possible move to up left side from bishop
        # input : pos [Position]
        # output: result [list of Position]
        result = []
        x = pos.x
        y = pos.y
        while (y < self.MAXSIZE - 1) and (x > self.MINSIZE + 1):
            pos_temp = Position(x - 1, y + 1)
            result.append(pos_temp)
            x = x - 1
            y = y + 1
        return result

    def possible_move_up_right(self, pos):
        # this method calculates possible move to up right side from bishop
        # input : pos [Position]
        # output: result [list of Position]
        result = []
        x = pos.x
        y = pos.y
        while (y < self.MAXSIZE - 1) and (x < self.MAXSIZE - 1):
            pos_temp = Position(x + 1, y + 1)
            result.append(pos_temp)
            x = x + 1
            y = y + 1
        return result

    def possible_move_down_left(self, pos):
        # this method calculates possible move to down left side from bishop
        # input : pos [Position]
        # output: result [list of Position]
        result = []
        x = pos.x
        y = pos.y
        while (y > self.MINSIZE - 1) and (x > self.MINSIZE + 1):
            pos_temp = Position(x - 1, y - 1)
            result.append(pos_temp)
            x = x - 1
            y = y - 1
        return result

    def possible_move_down_right(self, pos):
        # this method calculates possible move to down right side from bishop
        # input : pos [Position]
        # output: result [list of Position]
        result = []
        x = pos.x
        y = pos.y
        while (y > self.MINSIZE - 1) and (x < self.MAXSIZE - 1):
            pos_temp = Position(x + 1, y - 1)
            result.append(pos_temp)
            x = x + 1
            y = y - 1
        return result

    def show_possible_moves(self, position=None):
        # this method returns a list containing all possible moves that
        # can be done by this object
        # input : position [Position]
        # output: result [list of Position]

        result = []
        pos = position if position is not None else self.position

        result.append(self.possible_move_up_left(pos))
        result.append(self.possible_move_up_right(pos))
        result.append(self.possible_move_down_left(pos))
        result.append(self.possible_move_down_right(pos))

        return result

    def draw(self):
        # this method prints Bishop symbol 'B'
        # input : None
        # output: 'B'
        print('B', end='')

# bishop = Bishop()
# pos = Position(4,4)
# res = bishop.show_possible_moves(pos)

# for x in res:
#     for y in x:
#         y.print_attribute()
#     print()
