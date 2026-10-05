class Shape:
	def area(self):
		print("Метод AREA должен быть определен")

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
