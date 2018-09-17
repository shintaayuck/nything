
class Position:

    def __init__ (self , x = 0 , y = 0):
        self.x = x
        self.y = y


    def copy(self, pos):
        self.x = getattr(pos,'x')
        self.y = getattr(pos,'y')

    def printAtribute(self):
        print("(",self.x, ",", self.y,")", end=' ')

    def getCordinate(self):
        return "("+str(self.x) +","+ str(self.y)+")"