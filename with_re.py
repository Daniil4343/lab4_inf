import re

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


print(f"Файл: {day}3.yaml")

with open(f"{day}.json", 'r', encoding='utf-8') as file:
    data = file.read()

yaml_lines = []
indent = "  "


pattern = re.compile(r'"(.*?)"\s*:\s*(.*?)(?:,|$)')


data = re.sub(r'^\{|\}$', '', data.strip())


lines = data.splitlines()
for line in lines:
    line = line.strip().rstrip(",")
    if line.endswith("{") or line.endswith("}"):
        continue
    match = pattern.match(line)
    if match:
        key = match.group(1).strip()
        value = match.group(2).strip().strip('"')
        yaml_lines.append(f"{indent}{key}: {value}")
    else:
        yaml_lines.append(f"- {line.strip()}")

with open(f"{day}3.yaml", 'w', encoding='utf-8') as file:
    file.write('\n'.join(yaml_lines))

