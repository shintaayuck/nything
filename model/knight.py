from position import Position


class Knight:

    # Constants
    MAXSIZE = 8
    MINSIZE = 0
    RELATIVE_MOVEMENT = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2),
                         (-1, 2), (1, -2), (1, 2)]

    def __init__(self, pos=Position(), color=True):
        # type: (Position, bool) -> None
        self.__position = pos
        self.__color = color

    @property
    def position(self):
        # type: () -> Position
        return self.__position

    @position.setter
    def position(self, pos):
        # type (Position) -> None
        self.__position = pos

    @property
    def color(self):
        # type: () -> bool
        return self.__color

    @color.setter
    def color(self, color):
        # type (bool) -> None
        self.__color = color

    def show_possible_moves(self, position=None):
        # type: () -> list
        li = []

        my_position = position if position is not None else self.position
        my_x, my_y = my_position.x, my_position.y

        # as tuple unpacking is gone in Python 3, must find a workaround
        # for lambda function
        valid_position = lambda point: (point[0] >= self.MINSIZE and
                                        point[1] >= self.MINSIZE)\
            and (point[0] < self.MAXSIZE and
                 point[1] < self.MAXSIZE)
        moves = lambda point: (my_x + point[0], my_y + point[1])
        temp_li = filter(valid_position, map(moves, self.RELATIVE_MOVEMENT))

        for pos in temp_li:
            pos_temp = Position(pos[0], pos[1])
            li.append(pos_temp)

        return li

    def draw(self):
        # this method prints Bishop symbol 'K'
        # input : None
        # output: 'K'
        if(self.__color):
            print('K ', end='')
        else:
            print('k ', end='')
