lines = [
    "4pqnrmqlscq1fkzxngndmgseven2",
    "5gcnnbjcgqn7",
    "68four4htvj8bk",
    "vxqmbgjnr6one"
]

total = 0

for line in lines:
    digits = [char for char in line if char.isdigit()]

    value = int(digits[0] + digits[-1])
    total += value
    print(f"Рядок: {line}, Значення: {value}")

print(f"Сума всіх значень: {total}")