from position import Position


class Knight:

    # Constants
    MAXSIZE = 8
    MINSIZE = 8
    RELATIVE_MOVEMENT = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    def __init__(self, pos = Position(), color = True):
        # type: (Position, bool) -> None
        self.__position = pos
        self.__color = color


    @property
    def position(self):
        # type: () -> Position
        return self.__position
    

    @position.setter
    def position(self, pos):
        #type (Position) -> None
        self.__position = pos


    @property    
    def color(self):
        #type: () -> bool
        return self.__color()


    @color.setter
    def color(self, color):
        #type (bool) -> None
        self.__color = color


    def show_possible_moves(self):
        # type: () -> list
        li = []
        current_x, current_y = self.position.x, self.position.y

        # as tuple unpacking is gone in Python 3, must find a workaround for lambda function
        valid_position = lambda point : (point[0] >= 0 and point[1] >= 0)\
                                        and (point[0] < 8 and point[0] < 8)
        moves = lambda point : (current_x + point[0], current_y + point[1])
        temp_li = filter(valid_position, map(moves, self.RELATIVE_MOVEMENT))

        for pos in temp_li:
            pos_temp = Position(pos[0], pos[1])
            li.append(pos_temp)

        return li


if __name__ == '__main__':
    # Unit test
    poses = [Position(0,0), Position(7,0), Position(7,7), Position(0,7), Position(4,4)]

    for i, pos in enumerate(poses):
        print('Knight {} - Pos: ({},{})'.format(i, pos.x, pos.y))
        
        k = Knight(pos, True)
        
        moves = k.show_possible_moves()
        for move in moves:
            print('({},{})'.format(move.x, move.y))