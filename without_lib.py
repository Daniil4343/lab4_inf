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


print(f"Файл: {day}.yaml")

with open(f"{day}.json", 'r', encoding='utf-8') as file:
    data = file.read()

yaml_lines = []
indent = "  "
for line in data.splitlines():
    line = line.strip().rstrip(",")
    if line.endswith("{") or line.endswith("}"):
        continue
    if ":" in line:
        key, value = line.split(":", 1)
        key = key.strip().replace('"', '')
        value = value.strip().replace('"', '')
        yaml_lines.append(f"{indent}{key}: {value}")
    else:
        yaml_lines.append(f"- {line.strip()}")

with open(f"{day}.yaml", 'w', encoding='utf-8') as file:
    file.write('\n'.join(yaml_lines))

