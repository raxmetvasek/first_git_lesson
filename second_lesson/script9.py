from abc import ABC, abstractmethod
class Shape(ABC):
	@abstractmethod
	def area (self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		return 3.14*self.radius**2

class Square(Shape):
	def __init__(self, side):
		self.side = side
	def area(self):
		return self.side**2
sq = Square(10)
