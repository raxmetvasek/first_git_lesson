from sqlalchemy import update, delete
with engine.connect() as connection:
	statement = (
		update(students_table)
		.where(students_table.c.name == 'Петров П.П.')
		.values(gpa = 4.6)
		)
	result = connection.execute(statement)
	connection.commit()
	print(f'Обновлено строк: {result.rowcount}')
	"""пример с delete"""
	statement2 = delete(students_table).where(students_table.c.gpa < 3.5)
	result2 = connection.execute(statement2)
	connection.commit()
