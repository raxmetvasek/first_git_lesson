def bread(func):
	def wrapper():
		print()
		func()
		print("<\_____/>")
	return wrapper
def ingredients(func):
	def wrapper():
		print('#Помидор')
		func()
		print('~салат~')
	return wrapper
def sandwich(food='--ветчина--'):
	print(food)
sandwich = bread(ingredients(sandwich))
sandwich()

print()
print()
@bread
@ingredients
def sandwic(food='---ветчина---'):
	print(food)
sandwic()

