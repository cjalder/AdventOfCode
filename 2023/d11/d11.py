import numpy as np
from itertools import combinations
import math

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

# with open("input.txt") as fh:
#     test_input = fh.read()

dat = []
for line in test_input.splitlines():
    dat.append([i for i in line])

universe = np.matrix(dat)

rows = []
cols = []
for i in range(len(universe)):
    if np.all(universe[i,:] == "."):
        rows.append(i)
    if np.all(universe[:,i] == "."):
        cols.append(i)

for i,r in enumerate(rows):
    universe = np.insert(universe, i+r, ".", axis = 0)
for i,c in enumerate(cols):
    universe = np.insert(universe, i+c, ".", axis = 1)

galaxies = list(combinations((zip(*np.where(universe == "#"))),2))


part1 = []
for (ix,iy),(jx,jy) in galaxies:
    dist = abs(ix-jx) + abs(iy-jy)
    part1.append(dist)

print(sum(part1))

# part 2 
universe = np.matrix(dat)
galaxies = list(combinations((zip(*np.where(universe == "#"))),2))
expansion = 1000000
part2 =[]
for (ix,iy),(jx,jy) in galaxies:
    dist = abs(ix-jx) + abs(iy-jy)
    for i in range(*sorted([ix, jx])):
        if i in rows:
            dist += (expansion-1)
    for i in range(*sorted([iy, jy])):
        if i in cols:
            dist += (expansion-1)
    part2.append(dist)
print(sum(part2))



