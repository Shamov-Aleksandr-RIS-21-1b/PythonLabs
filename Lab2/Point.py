class Point(object):
	def __new__(cls, *args, **kwargs):
        return super(object, self).__new__(cls)

	def __init__(self, x, y):
		self.x = x
		self.y = y


		
