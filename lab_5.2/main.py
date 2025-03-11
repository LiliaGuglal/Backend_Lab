games = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

limits = {"red": 12, "green": 13, "blue": 14}

total_id_sum = 0

for game in games:
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