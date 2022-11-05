from abc import ABC, abstractmethod, abstractproperty
from point import Point

class Shape(ABC):

	@abstractmethod
	@property
	def points(self):
		return self._points

	@abstractmethod
	@points.setter
	def points(self, *args):
		self._points = points_to_array(*args)

    @abstractmethod
    def get_square(self):
    	pass