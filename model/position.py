class Position :
	'Position of an object in 2 dimensions'
	#constructor
	def __init__(self, x = None, y = None) :
		self.__x = x if x is not None else 0
		self.__y = y if y is not None else 0
	#getters and setters
	@property
	def x(self) :
		return self.__x

	@property
	def y(self) :
		return self.__y

	@x.setter
	def x(self, x) :
		self.__x = x

	@y.setter
	def y(self, y) :
		self.__y = y

	def print_attribute(self) :
		print ("(",self.x,",",self.y,")")
