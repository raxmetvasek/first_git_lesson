from sqlalchemy import select

with engine.connect() as connection:
	statement = select(students_table)
	result = connection.execute(statement)
	for row in result:
		print(row.id, row.name, row.is_active)

	statement2 = select(students_table.c.name, students_table.c.gpa)
	result2 = connection.execute(statement2)
	for row in result2:
		print(row.name, row.gpa)
