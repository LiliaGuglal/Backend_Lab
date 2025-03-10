reports = [
    [5, 1, 5, 4, 5],
    [6, 5, 8, 5, 9],
    [6, 0, 6, 3, 7],
    [9, 7, 5, 4, 3],
    [8, 6, 4, 4, 1],
    [1, 2, 3, 5, 6]
]


def is_safe(report):
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    if not (increasing or decreasing):
        return False
    
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 2:
            return False
    
    return True


safe_count = 0
for report in reports:
    if is_safe(report):
        safe_count += 1
        print(f"Безпечний звіт: {report}")
    else:
        print(f"Небезпечний звіт: {report}")
print(f"Кількість безпечних звітів: {safe_count}")