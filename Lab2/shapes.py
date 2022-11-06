from abc import ABC, abstractmethod, abstractproperty
from coordinates import *

class Shape(ABC):

	@property
	@abstractmethod
	def points(self):
		return _points

	@points.setter
	@abstractmethod
	def points(self, plist):
		if not self.is_points_list(plist):
			raise TypeError("some of parametrs was not the Point")
		self._points = plist

	@staticmethod
	def is_points_list(plist):
		for i in range(len(plist)):
			if not isinstance(plist[i], Point):
				return False
		return True

	@abstractmethod
	def get_square(self):
		pass

class Triangle(Shape):

	def __init__(self, plist):
		self.points = plist

	@property
	def points(self):
		return super(Triangle, type(self)).points

	@points.setter
	def points(self, plist):
		if len(plist) != 3:
			raise AttributeError("too few or too many elements")
		super(Triangle, type(self)).points.fset(self, plist)

	def get_square(self):
		vect01 = Vector().set_from_points(self.points[0], self.points[1])
		vect02 = Vector().set_from_points(self.points[0], self.points[2])
		side02 = Point.distance(self.points[0], self.points[2])
		subside02 = Vector.scalarprod(vect01, vect02) / side02
		side01 = Point.distance(self.points[0], self.points[1])
		height = (side01 ** 2 - subside02 ** 2) ** 0.5
		return height * side01 / 2