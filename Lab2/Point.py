class Point():

	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		if not isinstance(x, int) or not isinstance(x, float):
			raise TypeError("Error: parametr was not the number.")
		self._x = x

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, y):
		if not isinstance(y, int) or not isinstance(y, float):
			raise TypeError("Error: parametr was not the number.")
		self._y = y

	@staticmethod
	def points_to_array(*args):
    	if not isinstance(args, Point):
    		raise TypeError("Error: Some of parametrs was not the Point.")
    	return [*args]

    @staticmethod
    def distance(p1, p2):
    	if not isinstance(p1, Point) or not isinstance(p2, Point):
    		raise TypeError("Error: Some of parametrs was not the Point.")
    	return ((p1.x - p2.x) ** 2 + (p1.x - p2.x) ** 2) ** 0.5