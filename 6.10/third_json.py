import json

with open("students_db.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    if student["is_active"] = True:
        student["scholarship"] = 0
        student["is_active"] = False
        with open("updated_students_db.json", "w", encoding="utf-8") as f_new:
            st=json.dump(students, f_new, indent=4, ensure_ascii=False)
        print("Изменения сохранены в файл", st)
