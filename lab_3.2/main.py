file_path = "input_2.txt"

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Файл {file_path} не знайдено.")
    exit(1)
except Exception as e:
    print(f"Помилка під час читання файлу: {e}")
    exit(1)

total = 0

for line in lines:
    line = line.strip() 
    digits = [char for char in line if char.isdigit()]

    if len(digits) >= 2: 
        value = int(digits[0] + digits[-1])
        total += value
        print(f"Рядок: {line}, Значення: {value}")
    else:
        print(f"Рядок: {line}, не містить достатньо цифр для обчислення значення.")

print(f"Сума всіх значень: {total}")
