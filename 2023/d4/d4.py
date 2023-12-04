test_input="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

with open("input.txt") as fh:
    test_input = fh.read()

part1 = []
part2 = {i:1 for i in range(1, len(test_input.splitlines())+1)}
for game, line in enumerate(test_input.splitlines(), 1):
    win, scratch = line.split(":")[-1].split("|")
    win = set([int(i) for i in win.split()])
    scratch = set([int(i) for i in scratch.split()])
    matching = len(win.intersection(scratch))
    if matching > 0:
        part1.append(2 ** (matching - 1))
    # part 2    
    copies = part2[game]
    for m in range(1,matching+1):
        part2[game+m] += copies

print(sum(part1))
print(sum(part2.values()))

