left = [2,6,8,4,8]
right = [7,6,5,1,1]

left.sort()
right.sort()

total_distance = 0
for i in range(len(left)):
    distance = abs(left[i] - right[i]) 
    total_distance += distance
    print(f"Пара: {left[i]} і {right[i]}, відстань: {distance}")

print(f"Загальна сума відстаней: {total_distance}")