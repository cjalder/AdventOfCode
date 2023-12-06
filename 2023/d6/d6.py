import re
import numpy as np

test_input="""Time:      7  15   30
Distance:  9  40  200"""

with open("input.txt") as fh:
    test_input = fh.read()

t, d = test_input.splitlines()
t = list(map(int, re.findall(r"([0-9]+)", t)))
d = list(map(int, re.findall(r"([0-9]+)", d)))
race = dict(zip(t,d))

part1 = []
for time, distance in race.items():
    won = 0
    for i in range(time+1):
        travel = i * (time - i)
        if travel > distance:
            won += 1
    part1.append(won)

print(np.prod(part1))

part2 = 0
time = int("".join([str(i) for i in t]))
distance = int("".join([str(i) for i in d]))
for i in range(time+1):
    travel = i * (time - i)
    if travel > distance:
        part2 += 1
print(part2)
