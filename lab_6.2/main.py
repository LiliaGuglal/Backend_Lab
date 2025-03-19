def calculate_score(filename):
    shape_points = {'X': 1, 'Y': 2, 'Z': 3}
    
    outcomes = {
        'A X': 3,  
        'A Y': 6,
        'A Z': 0, 
        'B X': 0,
        'B Y': 3, 
        'B Z': 6, 
        'C X': 6,  
        'C Y': 0, 
        'C Z': 3 
    }
    
    total_score = 0
    
    with open(filename, 'r') as file:
        for line in file:
            opponent, me = line.strip().split()
            total_score += shape_points[me]
            total_score += outcomes[f'{opponent} {me}']
    
    return total_score

example = """A Y
B X
C Z"""

with open('input_6.txt', 'w') as f:
    f.write(example)

score = calculate_score('input_6.txt')
print(f"Загальний рахунок: {score}")