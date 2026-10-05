class Cat:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def __str__(self):
		return f"Котик {self.name}, возраст: {self.age}"
	def __repr__(self):
		return f"Cat(name = '{self.name}', age = '{self.age}')"
 
cat = Cat("Вася", 3)
print(repr(cat))
