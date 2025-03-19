limits = {"red": 12, "green": 13, "blue": 14}

total_id_sum = 0

with open("input_5.txt", "r") as file:
    games = file.readlines()

for game in games:
    game = game.strip()  
    game_id = int(game.split(":")[0].split()[1])
    sets = game.split(":")[1].split(";")
    
    possible = True
    for game_set in sets:
        cubes = {"red": 0, "green": 0, "blue": 0}
        parts = game_set.split(",")
        for part in parts:
            count, color = part.strip().split()
            cubes[color] = int(count)

        if cubes["red"] > limits["red"] or cubes["green"] > limits["green"] or cubes["blue"] > limits["blue"]:
            possible = False
    
    
    if possible:
        total_id_sum += game_id
        print(f"Гра {game_id} можлива")
    else:
        print(f"Гра {game_id} неможлива")

print(f"Сума ID можливих ігор: {total_id_sum}")
