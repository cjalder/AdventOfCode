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

with open("input.txt") as fh:
    test_input = fh.read()

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


galaxies = list(combinations((zip(*np.where(universe == "#"))),2))


expansion = 1000000
def galaxy_dist(galaxies, expansion):
    distances =[]
    for (ix,iy),(jx,jy) in galaxies:
        dist = abs(ix-jx) + abs(iy-jy)
        for i in range(*sorted([ix, jx])):
            if i in rows:
                dist += (expansion-1)
        for i in range(*sorted([iy, jy])):
            if i in cols:
                dist += (expansion-1)
        distances.append(dist)
    return sum(distances)

print(galaxy_dist(galaxies, 2))
print(galaxy_dist(galaxies, 1000000))



