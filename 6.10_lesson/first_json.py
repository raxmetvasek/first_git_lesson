import json
data={"name": "Иван",
     "is_student": True,
     "grades": [4, 5, 5]}
json_string=json.dumps(data, ensure_ascii=False, indent=4)
parsed_data=json.loads(json_string)
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii= False)
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data=json.load(f)
