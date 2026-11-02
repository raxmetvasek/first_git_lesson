import json

with open('users.json', 'r') as f:
	users = json.load(f)

cities_without_reiterations = {people['address']['city'] for people in users}

city_parsed = {city : [] for city in cities_without_reiterations}
for city in city_parsed.keys():
	for people in users:
		if people['address']['city'] == city:
			city_parsed[city].append(people['name'])

with open('cities.json', 'w') as c:
	json.dump(city_parsed, c, sort_keys = True, indent=2)

with open('cities.json', 'r') as f: 
	print(f.read())
