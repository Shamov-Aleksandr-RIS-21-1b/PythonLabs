from abc import ABC, abstractmethod, abstractproperty
from coordinates import *
from statistics import mean
import math

class Shape(ABC):

	@abstractmethod
	def _points_get(self):
		return self._points

	@abstractmethod
	def _points_set(self, plist):
		if not Shape.is_points_list(plist):
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

	def __init__(self, p0, p1, p2):
		self._points_set([p0, p1, p2])

	def _points_get(self):
		return super(Triangle, type(self))._points_get(self)

	def _points_set(self, plist):
		if len(plist) != 3:
			raise AttributeError("too few or too many elements")
		super(Triangle, type(self))._points_set(self, plist)
		if not Triangle.is_exist(self.points[0], self.points[1], self.points[2]):
			raise AttributeError("this triangle is not exists")

	points = property(_points_get, _points_set)

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

	@staticmethod
	def is_exist(p0, p1, p2):
		if not isinstance(p0, Point) or not isinstance(p2, Point) or not isinstance(p2, Point):
			raise TypeError("some of parameters was not the Point")
		deltax = p2.x - p1.x
		mdeltay = p1.y - p2.y
		if deltax == 0:
			if deltay == 0:
				return False
			elif p0.x == p1.x:
				return False
			else:
				return True
		k = (p1.y - p2.y) / deltax
		b = (p1.x * p2.y - p2.x * p1.y) / deltax
		if p0.y == p0.x * k + b:
			return False
		return True

class Rectangle(Shape):

	def __init__(self, p0, p1, p2, p3):
		self._points_set([p0, p1, p2, p3])

	def _points_get(self):
		return super(Rectangle, type(self))._points_get(self)

	def _points_set(self, plist):
		if len(plist) != 4:
			raise AttributeError("too few or too many elements")
		super(Rectangle, type(self))._points_set(self, plist)

	points = property(_points_get, _points_set)

	def get_square(self):
		vect01 = Vector()
		vect01.set_from_points(self.points[0], self.points[1])
		side01 = vect01.modulus()
		vect03 = Vector()
		vect03.set_from_points(self.points[0], self.points[3])
		side03 = vect03.modulus()
		subside03 = Vector.scalarprod(vect01, vect03) / side03
		height = (side01 ** 2 - subside03 ** 2) ** 0.5
		return height * side03

class Ellipse(Shape):

	def __init__(self, center, shalfaxis, lhalfaxis):
		self._points_set(center)
		self.shalfaxis = NumberDescriptor("shalfaxis")
		self.lhalfaxis = NumberDescriptor("lhalfaxis")
		self.shalfaxis = shalfaxis
		self.lhalfaxis = lhalfaxis

	def _points_get(self):
		return super(Ellipse, type(self))._points_get(self)

	def _points_set(self, center):
		if not isinstance(center, Point):
			raise TypeError("parametr was not the Point")
		self._points = center

	center = property(_points_get, _points_set)

	def get_square(self):
		return math.pi * self.shalfaxis * self.lhalfaxis