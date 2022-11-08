from abc import ABC, abstractmethod, abstractproperty
from coordinates import *
from statistics import mean
from math import pi, sin

class PositiveNumberDescriptor(NumberDescriptor):
	def __set__(self, instance, value):
		if not isinstance(value, int | float):
			raise TypeError("parameter was not the number")
		if value <= 0:
			raise AttributeError(f"need positive number, value = {value}")
		instance.__dict__[self._name] = value

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
		vect01 = Vector.set_from_points(self.points[0], self.points[1])
		side01 = vect01.modulus()
		vect02 = Vector.set_from_points(self.points[0], self.points[2])
		side02 = vect02.modulus()
		subside02 = Vector.scalarprod(vect01, vect02) / side02
		height = (side01 ** 2 - subside02 ** 2) ** 0.5
		return height * side02 / 2

	@staticmethod
	def is_exist(p0, p1, p2):
		if not isinstance(p0, Point) or not isinstance(p1, Point) or not isinstance(p2, Point):
			raise TypeError("some of parameters was not the Point")
		deltax = p2.x - p1.x
		deltay = p2.y - p1.y
		if deltax == 0:
			if deltay == 0:
				return False
			elif p0.x == p1.x:
				return False
			else:
				return True
		k = deltay / deltax
		b = (p2.x * p1.y - p1.x * p2.y) / deltax
		return p0.y != p0.x * k + b

class Rectangle(Shape):

	def __init__(self, p0, p1, p2, p3):
		self._points_set([p0, p1, p2, p3])

	def _points_get(self):
		return super(Rectangle, type(self))._points_get(self)

	def _points_set(self, plist):
		if len(plist) != 4:
			raise AttributeError("too few or too many elements")
		super(Rectangle, type(self))._points_set(self, plist)
		if not Rectangle.is_exist(self.points[0], self.points[1], self.points[2], self.points[3]):
			raise AttributeError("this convex rectangle is not exists")

	points = property(_points_get, _points_set)

	def get_square(self):
		dvect02 = Vector.set_from_points(self.points[0], self.points[2])
		dvect13 = Vector.set_from_points(self.points[1], self.points[3])
		d02 = dvect02.modulus()
		d13 = dvect13.modulus()
		angle = Vector.get_angle(dvect02, dvect13)
		return d02 * d13 * sin(angle) / 2

	@staticmethod
	def is_exist(p0, p1, p2, p3):
		if (not Triangle.is_exist(p0, p1, p2) or 
			not Triangle.is_exist(p1, p2, p3) or 
			not Triangle.is_exist(p2, p3, p0) or 
			not Triangle.is_exist(p3, p0, p1)):
			return False
		deltax = p2.x - p1.x
		deltay = p2.y - p1.y
		if deltax == 0:
			if p0.x < p1.x:
				return p3.x < p1.x
			else:
				return p3.x > p1.x
		elif deltay == 0:
			if p0.y < p1.y:
				return p3.y < p1.y
			else:
				return p3.y > p1.y
		else: 
			k = deltay / deltax
			b = (p2.x * p1.y - p1.x * p2.y) / deltax
			if p0.y < k * p0.x + b:
				return p3.y < k * p3.x + b
			else:
				return p3.y > k * p3.x + b

class Ellipse(Shape):

	shalfaxis = PositiveNumberDescriptor("shalfaxis")
	lhalfaxis = PositiveNumberDescriptor("lhalfaxis")

	def __init__(self, center, shalfaxis, lhalfaxis):
		self._points_set(center)
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
		return pi * self.shalfaxis * self.lhalfaxis