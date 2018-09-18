class Position :
	'Position of an object in 2 dimensions'
	#constructor
	def __init__(self, x = None, y = None) :
		self.x = x if x is not None else 0
		self.y = y if y is not None else 0
	#getters and setters
	def get_x(self) :
		return self.x

	def get_y(self) :
		return self.y

	def set_x(self, x) :
		self.x = x

	def set_y(self, y) :
		self.y = y

	def print_attribute(self) :
		print ("(",self.get_x(),",",self.get_y(),")")
