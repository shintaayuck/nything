from position import Position

class Queen:
    MAXSIZE = 8
    MINSIZE = 0
    #constructor
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        print(self.pos.get_x()," ", self.pos.get_y()," ",self.color)

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
    def possible_move_up(self):
        result = []
        x = self.get_position().get_x()
        y = self.get_position().get_y()
        while (y < self.MAXSIZE-1) :
            pos_temp = Position(x,y+1)
            result.append(pos_temp)
            y = y+1
        return result

    def possible_move_down(self):
        result = []
        x = self.get_position().get_x()
        y = self.get_position().get_y()
        while (y > self.MINSIZE+1) :
            pos_temp = Position(x,y-1)
            result.append(pos_temp)
            y = y-1
        return result

    def possible_move_right(self):
        result = []
        x = self.get_position().get_x()
        y = self.get_position().get_y()
        while (x < self.MAXSIZE-1) :
            pos_temp = Position(x+1,y)
            result.append(pos_temp)
            x = x+1
        return result

    def possible_move_left(self):
        result = []
        x = self.get_position().get_x()
        y = self.get_position().get_y()
        while (x > self.MINSIZE+1) :
            pos_temp = Position(x-1,y)
            result.append(pos_temp)
            x = x-1
        return result

    def possible_move_up_left(self):
        result = []
        x = self.get_position().get_x()
        y = self.get_position().get_y()
        while (y < self.MAXSIZE-1) and (x > self.MINSIZE+1):
            pos_temp = Position(x-1,y+1)
            result.append(pos_temp)
            x = x-1
            y = y+1
        return result

    def possible_move_up_right(self):
        result = []
        x = self.get_position().get_x()
        y = self.get_position().get_y()
        while (y < self.MAXSIZE-1) and (x < self.MAXSIZE-1) :
            pos_temp = Position(x+1,y+1)
            result.append(pos_temp)
            x = x+1
            y = y+1
        return result

    def possible_move_down_left(self):
        result = []
        x = self.get_position().get_x()
        y = self.get_position().get_y()
        while (y > self.MINSIZE-1) and (x > self.MINSIZE+1):
            pos_temp = Position(x-1,y-1)
            result.append(pos_temp)
            x = x-1
            y = y-1
        return result

    def possible_move_down_right(self):
        result = []
        x = self.get_position().get_x()
        y = self.get_position().get_y()
        while (y > self.MINSIZE-1) and (x < self.MAXSIZE-1) :
            pos_temp = Position(x+1,y-1)
            result.append(pos_temp)
            x = x+1
            y = y-1
        return result

    def show_possible_moves(self):
        list = []
        list.append(self.possible_move_up())
        list.append(self.possible_move_up_right())
        list.append(self.possible_move_right())
        list.append(self.possible_move_down_right())
        list.append(self.possible_move_down())
        list.append(self.possible_move_down_left())
        list.append(self.possible_move_left())
        list.append(self.possible_move_up_left())
        return list

#
# p = Position(3,4)
# q = Queen(p, "white")
# list = q.possible_move_up() + q.possible_move_down() + q.possible_move_left() + q.possible_move_right()
# lists = q.possible_move_up_left() + q.possible_move_up_right() + q.possible_move_down_left() + q.possible_move_down_right()
# for l in lists:
#     print(l.get_x(), l.get_y())
