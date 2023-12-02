import re
import numpy as np 

# test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

with open("input.txt") as fh:
    test_input = fh.read()

max_colours = {
    "red": 12,
    "green": 13,
    "blue": 14
}

part1 = []
for line in test_input.splitlines():
    game_num, play = line.split(": ")
    poss = True
    for roll in play.split(";"):
        output = re.findall(r"([0-9]+) (red|blue|green)", roll)
        for i in output:
            if int(i[0]) > max_colours[i[1]]:
                poss = False
    if poss:
        part1.append(int(game_num.split(" ")[1]))

print(sum(part1))


part2=[]
for line in test_input.splitlines():
    min_colours = {
    "red": 0,
    "green": 0,
    "blue": 0
}
    game_num, play = line.split(": ")
    for roll in play.split(";"):
        output = re.findall(r"([0-9]+) (red|blue|green)", roll)
        for i in output:
            if int(i[0]) > min_colours[i[1]]:
                min_colours[i[1]] = int(i[0])
    part2.append(np.prod(list(min_colours.values())))

print(sum(part2))
