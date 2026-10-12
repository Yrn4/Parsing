import json

path = r"C:\Users\ropek\Downloads\Telegram Desktop\users.json"

with open(path, "r", encoding="utf-8") as file:
    users = json.load(file)

cities = {}

for user in users:
    city = user["address"]["city"]
    name = user["name"]

    if city not in cities:
        cities[city] = []

    cities[city].append(name)


output_path = r"C:\Users\ropek\Downloads\Telegram Desktop\users.json"

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(cities, file, ensure_ascii=False, indent=4)

print("Данные успешно сохранены!")
