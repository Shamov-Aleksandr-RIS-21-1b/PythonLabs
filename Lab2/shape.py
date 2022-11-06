from abc import ABC, abstractmethod, abstractproperty
from coordinates import *

class Shape(ABC):

	@property
	@abstractmethod
	def points(self):
		return self._points

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