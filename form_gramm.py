import time

print('Выберите:')
print('1. Понедельник')
print('2. Четверг')
print('3. json из интернета')
day = input()
while day not in ('1', '2', '3'):
    print('Введите 1, 2 или 3')
    day = input()
if day == '1':
    day = 'pn'
elif day == '2':
    day = 'cht'
else:
    day = 'parsed'

print(f"Файл: {day}4.yaml")

start_time = time.time()


with open(f"{day}.json", 'r', encoding='utf-8') as file:
    data = file.read()

yaml_lines = []
indent = "  "
indent_level = 0

def process_json_line(line, indent_level):
    global yaml_lines
    line = line.strip().rstrip(",")

    if line.endswith("{"):
        key = line[:-1].strip().replace('"', '').rstrip(":")
        yaml_lines.append(f"{indent * indent_level}{key}:")
        return indent_level + 1

    elif line.endswith("}"):
        return indent_level - 1

    elif ":" in line:
        key, value = line.split(":", 1)
        key = key.strip().replace('"', '').rstrip(":")
        value = value.strip().replace('"', '').strip()
        yaml_lines.append(f"{indent * indent_level}{key}: {value}")
        return indent_level

    elif line.endswith("["):
        key = line[:-1].strip().replace('"', '').rstrip(":")
        yaml_lines.append(f"{indent * indent_level}{key}:")
        return indent_level + 1

    elif line.endswith("]"):
        return indent_level - 1

    elif line:
        value = line.strip().replace('"', '')
        yaml_lines.append(f"{indent * indent_level}- {value}")
        return indent_level

    return indent_level

for line in data.splitlines():
    indent_level = process_json_line(line, indent_level)

with open(f"{day}4.yaml", 'w', encoding='utf-8') as file:
    file.write('\n'.join(yaml_lines[1:]))

end_time = time.time()
print(f"Время выполнения: {100 * (end_time - start_time):.5f}")
