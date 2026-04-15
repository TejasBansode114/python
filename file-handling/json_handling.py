import json

# Python to JSON
data = {"name": "John", "age": 30, "city": "New York"}

with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# JSON to Python
with open("data.json", "r") as json_file:
    data_loaded = json.load(json_file)
print(data_loaded)