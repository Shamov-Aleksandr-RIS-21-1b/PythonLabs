import shape

class Triangle(Shape):

	def __init__(self, p1, p2, p3):
		self.points.fset(self, p1, p2, p3)

	@property
	def points(self):
		return super().points

	@points.setter
	def points(self, p1, p2, p3):
		super().points.fset(self, p1, p2, p3)