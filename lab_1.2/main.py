file_path = "input_1.txt"

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Файл {file_path} не знайдено.")
    exit(1)
except Exception as e:
    print(f"Помилка під час читання файлу: {e}")
    exit(1)


if len(lines) < 2:
    print("Файл має містити принаймні два рядки чисел.")
    exit(1)

try:
    left = [int(x) for x in lines[0].strip().split()]
    right = [int(x) for x in lines[1].strip().split()]
except ValueError:
    print("Помилка: один із рядків містить некоректні дані. Переконайтеся, що всі елементи є цілими числами.")
    exit(1)

if len(left) != len(right):
    print("Помилка: списки повинні бути однакової довжини.")
    exit(1)

left.sort()
right.sort()

total_distance = 0
for i in range(len(left)):
    distance = abs(left[i] - right[i])
    total_distance += distance
    print(f"Пара: {left[i]} і {right[i]}, відстань: {distance}")

print(f"Загальна сума відстаней: {total_distance}")
