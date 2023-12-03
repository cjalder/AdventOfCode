import re

test_input="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

with open("input.txt") as fh:
    test_input = fh.read()

matrix = dict()
symbols = set()
cogs = []
for i, line in enumerate(test_input.splitlines()):
    matrix[i] = dict()
    for j, char in enumerate(line):
        matrix[i][j] = char
        if char.isdigit() is False and char != ".":
            symbols.add(char)
        if char == "*":
            cogs.append((i,j))


def get_adjacent(matrix, i, j):
    m = len(matrix) 
    n = len(matrix[j]) 
    adjacent = dict()
    if i > 0:
        adjacent[(i-1,j)] = matrix[i-1][j]
    if i+1 < m:
        adjacent[(i+1,j)] = matrix[i+1][j]
    if j > 0:
        adjacent[(i,j-1)] = matrix[i][j-1]
    if j+1 < n:
        adjacent[(i,j+1)] = matrix[i][j+1]
    #diagonals 
    if i > 0 and j > 0:
        adjacent[(i-1, j-1)] = matrix[i-1][j-1]
    if i+1 < m and j > 0:
        adjacent[(i+1,j-1)] = matrix[i+1][j-1]
    if i+1 < m and j+1 < n:
        adjacent[(i+1, j+1)] = matrix[i+1][j+1]
    if i > 0 and j+1 < n: 
        adjacent[(i-1,j+1)] = matrix[i-1][j+1]
    return adjacent

part1 = []
for i in matrix:
    n = len(matrix[i]) - 1 
    num = []
    parts = []
    for j in matrix[i]:
        if matrix[i][j].isdigit():
            num.append(matrix[i][j])
            adjacent = get_adjacent(matrix, i, j)
            parts.extend(list(adjacent.values()))
        else:
            if any(x in symbols for x in parts) and num:
                part1.append(int("".join(num)))
            num = []
            parts = []
        if j == n:
            if any(x in symbols for x in parts) and num:
                part1.append(int("".join(num)))
                
print(sum(part1))

part2 = 0
gears = {c:[] for c in cogs}

for i in matrix:
    n = len(matrix[i]) - 1 
    num = []
    parts = []
    for j in matrix[i]:
        if matrix[i][j].isdigit():
            num.append(matrix[i][j])
            adjacent = get_adjacent(matrix, i, j)
            parts.extend(list(adjacent.keys()))
        else:
            if num:
                for gear in gears:
                    if gear in parts:
                        gears[gear].append(int("".join(num)))
            num = []
            parts = []
        if j == n:
            if num:
                for gear in gears:
                    if gear in parts:
                        gears[gear].append(int("".join(num)))

for nums in gears.values():
    if len(nums) == 2:
        part2 += (nums[0]*nums[1])
        
print(part2)

    