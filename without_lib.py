import time
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

print(f"Файл: {day}1.yaml")

start_time = time.time()
with open(f"{day}.json", 'r', encoding='utf-8') as file:
    data = file.read()
    yaml_lines = ""
    for a in file:
        if (not "{" in a) and (not "}" in a) and (not "]" in a) or ("}," in a):
            yaml_lines += a.replace('"', "").replace("    ", "  ")[2:].replace("[\n", "\n-").replace("},\n", "-").replace(",", "")
    yaml_lines = yaml_lines.replace("-  ", "- ")

with open(f"{day}1.yaml", 'w', encoding='utf-8') as file:
    file.write(yaml_lines)
end_time = time.time()
print(f"Время выполнения: {100*(end_time - start_time):.5f}")