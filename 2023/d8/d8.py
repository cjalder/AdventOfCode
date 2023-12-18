import re 
from math import lcm
test_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
with open("input.txt") as fh:
    test_input = fh.read()

instructions, lines = test_input.split("\n\n")
path = dict()
for l in lines.splitlines():
    p, l, r = re.findall(r"(\w+)", l)
    path[p] = {"L": l, "R": r}

location = "AAA"

step = 0
while location != "ZZZ":
    for i in instructions:
        location = path[location][i]
        step += 1

all_a = [i for i in path.keys() if i[-1] == "A"]
all_z = [i for i in path.keys() if i[-1] == "Z"]

part2 = []
for a in all_a:
    location = a
    step = 0
    while location not in all_z:
        for i in instructions:
            location = path[location][i]
            step += 1
    print(a,location)
    part2.append(step)

print(lcm(*part2))
   