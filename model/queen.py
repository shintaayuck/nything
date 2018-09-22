from position import Position


class Queen:

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
    def set_position(self, pos):
        self.__position = pos

    @color.setter
    def set_color(self, color):
        self.__color = color

    # methods
    def possible_move_up(self, pos):
        # this method calculates possible move to up left side from queen
        # input : pos [Position]
        # output: result [list of Position]
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y < self.MAXSIZE - 1):
            pos_temp = Position(x, y + 1)
            result.append(pos_temp)
            y = y + 1
        return result

    def possible_move_down(self, pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y > self.MINSIZE + 1):
            pos_temp = Position(x, y - 1)
            result.append(pos_temp)
            y = y - 1
        return result

    def possible_move_right(self, pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (x < self.MAXSIZE - 1):
            pos_temp = Position(x + 1, y)
            result.append(pos_temp)
            x = x + 1
        return result

    def possible_move_left(self, pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (x > self.MINSIZE + 1):
            pos_temp = Position(x - 1, y)
            result.append(pos_temp)
            x = x - 1
        return result

    def possible_move_up_left(self, pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y < self.MAXSIZE - 1) and (x > self.MINSIZE + 1):
            pos_temp = Position(x - 1, y + 1)
            result.append(pos_temp)
            x = x - 1
            y = y + 1
        return result

    def possible_move_up_right(self, pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y < self.MAXSIZE - 1) and (x < self.MAXSIZE - 1):
            pos_temp = Position(x + 1, y + 1)
            result.append(pos_temp)
            x = x + 1
            y = y + 1
        return result

    def possible_move_down_left(self, pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y > self.MINSIZE - 1) and (x > self.MINSIZE + 1):
            pos_temp = Position(x - 1, y - 1)
            result.append(pos_temp)
            x = x - 1
            y = y - 1
        return result

    def possible_move_down_right(self, pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y > self.MINSIZE - 1) and (x < self.MAXSIZE - 1):
            pos_temp = Position(x + 1, y - 1)
            result.append(pos_temp)
            x = x + 1
            y = y - 1
        return result

    def show_possible_moves(self, position=None):
        pos = position if position is not None else self.pos
        list = []
        list.append(self.possible_move_up(pos))
        list.append(self.possible_move_up_right(pos))
        list.append(self.possible_move_right(pos))
        list.append(self.possible_move_down_right(pos))
        list.append(self.possible_move_down(pos))
        list.append(self.possible_move_down_left(pos))
        list.append(self.possible_move_left(pos))
        list.append(self.possible_move_up_left(pos))
        return list


# p = Position(3,4)
# q = Queen(p, True)
# lists = q.show_possible_moves()
# for ls in lists:
#     for l in ls :
#         print(l.get_x(), l.get_y())
