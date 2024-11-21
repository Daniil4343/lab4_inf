import json
import yaml

print('Выберите:')
print('1. Понедельник')
print('2. Четверг')
print('3. json из интернета')
day = input()
while day not in ('1', '2','3'):
    print('Введите 1, 2 или 3')
    day = input()
if day == '1':
    day = 'pn'
elif day == '2':
     day = 'cht'
else:
    import parser
    day = 'parsed'


with open(f"{day}.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

with open(f'{day}2.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, allow_unicode=True, sort_keys=False)

print(f"Файл: {day}2.yaml")
