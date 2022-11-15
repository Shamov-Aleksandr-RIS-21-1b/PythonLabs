from abc import ABC, abstractmethod
from coordinates import *
from statistics import mean
from math import pi, sin
from jsoner import *

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

	@abstractmethod
	def get_json_data(self):
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
			if p0.x == p1.x:
				return False
			return True
		k = deltay / deltax
		b = (p2.x * p1.y - p1.x * p2.y) / deltax
		return p0.y != p0.x * k + b

	def get_json_data(self):
		return {'points' : [self.points[0].get_json_data(), self.points[1].get_json_data(), self.points[2].get_json_data()]}

	@classmethod
	def from_json(cls, data):
		return cls(Point.from_json(data['points'][0]), Point.from_json(data['points'][1]), Point.from_json(data['points'][2]))

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
		return d02 * d13 * abs(sin(angle)) / 2

	@staticmethod
	def is_exist(p0, p1, p2, p3):
		deltax02 = p2.x - p0.x
		deltax13 = p3.x - p1.x
		deltay02 = p2.y - p0.y
		deltay13 = p3.y - p1.y
		if deltax02 == 0:
			if deltax13 == 0:
				return False
			k13 = deltay13 / deltax13
			b13 = (p3.x * p1.y - p1.x * p3.y) / deltax13
			x_intersect = p0.x
			intersection = Point(x_intersect, k13 * x_intersect + b13)
		elif deltax13 == 0:
			if deltax02 == 0:
				return False
			x_intersect = p1.x
			k02 = deltay02 / deltax02
			b02 = (p2.x * p0.y - p0.x * p2.y) / deltax02
			intersection = Point(x_intersect, k02 * x_intersect + b02)
		else:
			k02 = deltay02 / deltax02
			k13 = deltay13 / deltax13
			if k02 == k13:
				return False
			b02 = (p2.x * p0.y - p0.x * p2.y) / deltax02
			b13 = (p3.x * p1.y - p1.x * p3.y) / deltax13
			x_intersect = (b13 - b02) / (k02 - k13)
			intersection = Point(x_intersect, k02 * x_intersect + b02)
		return (Point.distance(intersection, p0) + Point.distance(intersection, p2) == Point.distance(p0, p2) 
			and Point.distance(intersection, p1) + Point.distance(intersection, p3) == Point.distance(p1, p3))

	def get_json_data(self):
		return {'points' : [self.points[0].get_json_data(), self.points[1].get_json_data(), self.points[2].get_json_data(), self.points[3].get_json_data()]}

	@classmethod
	def from_json(cls, data):
		return cls(Point.from_json(data['points'][0]), Point.from_json(data['points'][1]), Point.from_json(data['points'][2]), Point.from_json(data['points'][3]))

class Ellipse(Shape):

	xhalfaxis = PositiveNumberDescriptor("xhalfaxis")
	yhalfaxis = PositiveNumberDescriptor("yhalfaxis")

	def __init__(self, center, xhalfaxis, yhalfaxis):
		self._points_set(center)
		self.xhalfaxis = xhalfaxis
		self.yhalfaxis = yhalfaxis

	def _points_get(self):
		return super(Ellipse, type(self))._points_get(self)

	def _points_set(self, center):
		if not isinstance(center, Point):
			raise TypeError("parametr was not the Point")
		self._points = center

	center = property(_points_get, _points_set)

	def get_square(self):
		return pi * self.xhalfaxis * self.yhalfaxis

	def get_json_data(self):
		return {'center' : self.center.get_json_data(), 'xhalfaxis' : self.xhalfaxis, 'yhalfaxis' : self.yhalfaxis}

	@classmethod
	def from_json(cls, data):
		return cls(Point.from_json(data['center']), data['xhalfaxis'], data['yhalfaxis'])