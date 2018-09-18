from position import Position


class Knight:

    # Constants
    MAXSIZE = 8
    MINSIZE = 8
    RELATIVE_MOVEMENT = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    def __init__(self, pos, color):
        # type: (Position, str) -> None
        self._position = pos
        self._color = color

    
    def position(self):
        # type: () -> Position
        return self._position.get_x(), self._position.get_y()


    def pos_x(self):
        # type: () -> int
        return self._position.get_x()

    
    def pos_y(self):
        # type: () -> int
        return self._position.get_y()

    
    def color(self):
        #type: () -> str
        return self.color()
    

    def set_position(self, pos):
        # type: Position -> None
        self._position = pos

    
    def show_possible_moves(self):
        # type: () -> list
        li = []
        current_x, current_y = self.position()

        valid_position = lambda (x, y) : x >= 0 and y >= 0
        moves = lambda (x, y) : (current_x + x, current_y + y)
        temp_li = filter(valid_position, map(moves, self.RELATIVE_MOVEMENT))

        for pos in temp_li:
            pos_temp = Position(pos[0], pos[1])
            li.append(pos_temp)

        return li


if __name__ == '__main__':
    # For testing purposes
    p = Position(4, 4)
    k = Knight(p, 'black')
    li = k.show_possible_moves()
    for pos in li:
        print pos.get_x(),pos.get_y()