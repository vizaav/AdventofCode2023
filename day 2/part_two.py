"""
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""
sum_of_powers = 0
with open("input.txt") as f:
    data = f.read().splitlines()

for game in data:
    game_possible = True
    # Split game into game_id and cubes
    game_id, cubes = game.split(":")
    game_id = int(game_id.split(" ")[1])
    cubes = cubes.split(";")

    # Remove whitespace and split cubes
    for i in range(len(cubes)):
        cubes[i] = cubes[i].split(",")
        for j in range(len(cubes[i])):
            cubes[i][j] = cubes[i][j].strip()

    # Check if game is possible
    for cube in cubes:
        for i in cube:
            cube_color = i.split(" ")[1]
            cube_amount = int(i.split(" ")[0])
    lowest_green = 0
    lowest_red = 0
    lowest_blue = 0

    for cube in cubes:
        for i in cube:
            cube_color = i.split(" ")[1]
            cube_amount = int(i.split(" ")[0])
            if cube_color == "green":
                if cube_amount > lowest_green:
                    lowest_green = cube_amount
            elif cube_color == "red":
                if cube_amount > lowest_red:
                    lowest_red = cube_amount
            elif cube_color == "blue":
                if cube_amount > lowest_blue:
                    lowest_blue = cube_amount

    sum_of_powers += lowest_green * lowest_red * lowest_blue

print(sum_of_powers)



