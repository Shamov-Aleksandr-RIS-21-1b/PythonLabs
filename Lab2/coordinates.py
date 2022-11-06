class Point():

	def __init__(self, x = None, y = None):
		if x is None:
			x = 0
		if y is None:
			y = 0
		self.x = x
		self.y = y

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		if not isinstance(x, int) and not isinstance(x, float):
			raise TypeError("parameter was not the number")
		self._x = x

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, y):
		if not isinstance(y, int) and not isinstance(y, float):
			raise TypeError("parameter was not the number")
		self._y = y

	@staticmethod
	def distance(p1, p2):
		if not isinstance(p1, Point) or not isinstance(p2, Point):
			raise TypeError("some of parameters was not the Point")
		return ((p1.x - p2.x) ** 2 + (p1.x - p2.x) ** 2) ** 0.5

class Vector(Point):

	def __init__(self, x = None, y = None):
		super(Vector, type(self)).__init__(self, x, y)

	def set_from_points(self, p1, p2)
		if not isinstance(p1, Point) or not isinstance(p2, Point):
			raise TypeError("some of parameters was not the Point")
		self.x = p2.x - p1.x
		self.y = p2.y - p1.y

	@staticmethod
	def scalarprod(v1, v2):
		if not isinstance(v1, Vector) or not isinstance(v2, Vector):
			raise TypeError("some of parameters was not the Vector")
		return v1.x * v2.x + v1.y * v2.y