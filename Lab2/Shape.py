from abc import ABCMeta, abstractmethod, abstractproperty

class Shape(metaclass = ABCMeta):

    @abstractmethod
    def get_square():
    	pass

    @abstractproperty
    def points(self):
    	pass