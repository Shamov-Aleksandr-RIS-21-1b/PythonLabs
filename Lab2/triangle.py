from shape import *

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

	def get_square():
		pass