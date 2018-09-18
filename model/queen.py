from position import Position

class Queen:
    MAXSIZE = 8
    MINSIZE = 0
    #constructor
    def __init__(self, pos = Position(), color = True):
        self.pos = pos
        self.color = color

    #getter
    def get_position(self):
        return self.pos

    def get_color(self):
        return self.color

    #setter
    def set_position(self,pos):
        self.pos = pos

    def set_color(self, color):
        self.color = color

    #possible_move
    def possible_move_up(self,pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y < self.MAXSIZE-1) :
            pos_temp = Position(x,y+1)
            result.append(pos_temp)
            y = y+1
        return result

    def possible_move_down(self,pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y > self.MINSIZE+1) :
            pos_temp = Position(x,y-1)
            result.append(pos_temp)
            y = y-1
        return result

    def possible_move_right(self,pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (x < self.MAXSIZE-1) :
            pos_temp = Position(x+1,y)
            result.append(pos_temp)
            x = x+1
        return result

    def possible_move_left(self,pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (x > self.MINSIZE+1) :
            pos_temp = Position(x-1,y)
            result.append(pos_temp)
            x = x-1
        return result

    def possible_move_up_left(self,pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y < self.MAXSIZE-1) and (x > self.MINSIZE+1):
            pos_temp = Position(x-1,y+1)
            result.append(pos_temp)
            x = x-1
            y = y+1
        return result

    def possible_move_up_right(self,pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y < self.MAXSIZE-1) and (x < self.MAXSIZE-1) :
            pos_temp = Position(x+1,y+1)
            result.append(pos_temp)
            x = x+1
            y = y+1
        return result

    def possible_move_down_left(self,pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y > self.MINSIZE-1) and (x > self.MINSIZE+1):
            pos_temp = Position(x-1,y-1)
            result.append(pos_temp)
            x = x-1
            y = y-1
        return result

    def possible_move_down_right(self,pos):
        result = []
        x = pos.get_x()
        y = pos.get_y()
        while (y > self.MINSIZE-1) and (x < self.MAXSIZE-1) :
            pos_temp = Position(x+1,y-1)
            result.append(pos_temp)
            x = x+1
            y = y-1
        return result

    def show_possible_moves(self,position = None):
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
