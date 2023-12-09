import numpy as np 

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

with open("input.txt") as fh:
    test_input = fh.read()

part1 = []
part2 = []
for line in test_input.splitlines():
    steps = []
    steps_2 = []
    current = list(map(int, line.split()))
    while all(x == 0 for x in current) is False:
        steps.insert(0, current[-1])
        current = np.diff(current)
    part1.append(sum(steps))

print(sum(part1))


part2 = []
for line in test_input.splitlines():
    steps = []
    current = list(map(int, line.split()))
    current.reverse()
    while all(x == 0 for x in current) is False:
        steps.insert(0, current[-1])
        current = np.diff(current)
    part2.append(sum(steps))

print(sum(part2))
