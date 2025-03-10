left = [3, 4, 2, 1, 3, 3]
right = [4, 3, 5, 3, 9, 3]

left.sort()
right.sort()

total_distance = 0
for i in range(len(left)):
    distance = abs(left[i] - right[i]) 
    total_distance += distance
    print(f"Пара: {left[i]} і {right[i]}, відстань: {distance}")

print(f"Загальна сума відстаней: {total_distance}")