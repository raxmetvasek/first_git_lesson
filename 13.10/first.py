import json

source = 'users.json'
result= 'users1.json'
iterations=100000

with open(source, 'r', encoding= 'utf-8') as f:
    data=json.load(f)
        
json_string=json.dumps(data, ensure_ascii=False)
    
with open(result, 'w', encoding='utf-8') as f:
    for _ in range(iterations):
        f.write(json_string + '\n')
            
print(f"Created! {result}")
