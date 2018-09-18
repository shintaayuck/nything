from position import Position


class Knight:

    # Constants
    MAXSIZE = 8
    MINSIZE = 8
    RELATIVE_MOVEMENT = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    def __init__(self, pos = Position(), color = True):
        # type: (Position, bool) -> None
        self._position = pos
        self._color = color

    
    def position(self):
        # type: () -> Position
        return self._position


    def pos_x(self):
        # type: () -> int
        return self._position.get_x()

    
    def pos_y(self):
        # type: () -> int
        return self._position.get_y()

    
    def color(self):
        #type: () -> bool
        return self.color()
    

    def set_position(self, pos):
        # type: Position -> None
        self._position = pos

    
    def show_possible_moves(self):
        # type: () -> list
        li = []
        current_x, current_y = self.position().get_x(), self.position().get_y()

        valid_position = lambda (x, y) : (x >= 0 and y >= 0) and (x < 8 and y < 8)
        moves = lambda (x, y) : (current_x + x, current_y + y)
        temp_li = filter(valid_position, map(moves, self.RELATIVE_MOVEMENT))

        for pos in temp_li:
            pos_temp = Position(pos[0], pos[1])
            li.append(pos_temp)

        return li


if __name__ == '__main__':
    # Unit test
    poses = [Position(0,0), Position(7,0), Position(7,7), Position(0,7), Position(4,4)]

    for i, pos in enumerate(poses):
        print 'Knight {} - Pos: ({},{})'.format(i, pos.get_x(), pos.get_y())
        
        k = Knight(pos, True)
        
        moves = k.show_possible_moves()
        for move in moves:
            print '({},{})'.format(move.get_x(), move.get_y())