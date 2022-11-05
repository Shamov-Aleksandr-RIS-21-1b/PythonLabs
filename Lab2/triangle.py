import shape

class Triangle(Shape):

	@property
	def points(self):
		return super().points

	@points.setter
	def points(self, *args):
		super().points.fset(self, *args)