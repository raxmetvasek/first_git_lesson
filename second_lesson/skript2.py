def my_shiny_new_decorator(function_to_decorate):
	def the_wrapper_around_the_original_function():
		print('Я - код, который отработает ДО вызова функции')
		function_to_decorate()
		print("А я код, который отработает ПОСЛЕ")
	return the_wrapper_around_the_original_function
def stand_alone_function():
	print('Я простая функция, и я не хочу изменений')
stand_alone_function_decorated=my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()
print()
@my_shiny_new_decorator
def another_stand_alone_function():
	print('Оставьте меня в покое')
another_stand_alone_function()

