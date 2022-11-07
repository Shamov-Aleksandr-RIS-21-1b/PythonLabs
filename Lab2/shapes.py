from abc import ABC, abstractmethod, abstractproperty
from coordinates import *

class Shape(ABC):

	@abstractmethod
	def points_get(self):
		return self._points

	@abstractmethod
	def points_set(self, plist):
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
		self.points_set(plist)

	def points_get(self):
		return super(Triangle, type(self)).points_get(self)

	def points_set(self, plist):
		if len(plist) != 3:
			raise AttributeError("too few or too many elements")
		super(Triangle, type(self)).points_set(self, plist)

	points = property(points_get, points_set)

	def get_square(self):
		vect01 = Vector()
		vect01.set_from_points(self.points[0], self.points[1])
		side01 = vect01.modulus()
		vect02 = Vector()
		vect02.set_from_points(self.points[0], self.points[2])
		side02 = vect02.modulus()
		subside02 = Vector.scalarprod(vect01, vect02) / side02
		height = (side01 ** 2 - subside02 ** 2) ** 0.5
		return height * side02 / 2