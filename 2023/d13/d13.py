import numpy as np

test_input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

with open ("input.txt") as fh:
    test_input = fh.read()

patterns = test_input.split("\n\n")

part1 = []
for pattern in patterns:
    matrix = []
    for line in pattern.splitlines():
        matrix.append([i for i in line])
    matrix = np.matrix(matrix)
    potential = []
    mirror = None
    for i in range(1, matrix.shape[1]):
        col1 = "".join( matrix[:,i-1].flatten().tolist()[0])
        col2 = "".join( matrix[:,i].flatten().tolist()[0])

        if col1 == col2:
            potential.append((i-1,i))
    for i,j in potential:
        ans = j
        reflection = True
        while i >= 0 and j < matrix.shape[1]:
            col1 = "".join( matrix[:,i].flatten().tolist()[0])
            col2 = "".join( matrix[:,j].flatten().tolist()[0])
            if col1 != col2:
                reflection = False
                break
            i -= 1
            j += 1
        if reflection is True:
            mirror = ans
    if mirror:
        part1.append(mirror)
        continue
    potential = []
    matrix = np.rot90(matrix)
    for i in range(1, matrix.shape[1]):
        col1 = "".join( matrix[:,i-1].flatten().tolist()[0])
        col2 = "".join( matrix[:,i].flatten().tolist()[0])
        if col1 == col2:
            potential.append((i-1,i))
    for i,j in potential:
        ans = j 
        reflection = True
        while i > 0  and j < matrix.shape[1]:
            col1 = "".join( matrix[:,i].flatten().tolist()[0])
            col2 = "".join( matrix[:,j].flatten().tolist()[0])
            if col1 != col2:
                reflection = False
                break
            i -= 1
            j += 1
        if reflection is True:
            mirror = ans * 100
    if mirror:
        part1.append(mirror)

print(sum(part1))

