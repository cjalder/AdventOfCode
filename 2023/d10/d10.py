test_input = """.....
.S-7.
.|.|.
.L-J.
....."""

with open("input.txt") as fh:
    test_input = fh.read()

matrix = {}
for i, line in enumerate(test_input.splitlines()):
    for j, l in enumerate(line):
        matrix[(j,i)] = l
        if l == "S":
            start = (j,i)


pipes = {
"|": [(0,-1), (0,1)], # N S
"-": [(1,0), (-1,0)], # E W
"L": [(0,-1), (1,0)], # N E 
"J": [(0,-1), (-1,0)], # N W
"7": [(0,1), (-1,0)], # S W
"F": [(0,1), (1,0)], # S E
"S": [(0,-1), (0,1), (1,0), (-1,0)]
}

# Checks if the pipe fits from direction your coming from
direction_dict = {
    (0,-1): ["|", "7", "F"],
    (0,1): ["|", "L", "J"],
    (1,0): ["J", "-", "7"],
    (-1,0): ["-", "L", "F"]
}




route = [start]
seen = []
while route:
    x,y = route.pop()
    p = matrix[(x,y)]
    for d, pipe in direction_dict.items():
        if d in pipes[p]:
            i, j = x+d[0], y+d[1]
            p_2 = matrix[(i,j)]
            if p_2 in pipe and (i,j) not in seen:
                route.append((i,j))
                seen.append((i,j))

print(len(seen)/2)




