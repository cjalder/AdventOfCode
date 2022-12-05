import re
from io import StringIO
import pandas as pd
test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def part1(crates,instructions):
    return None

def parse_crates(crates):
    crates = crates.split("\n")
    keys = crates[-1].split()
    # print(keys)
    nested = []
    for c in crates[:-1]:
        tmp = []
        for i in range(1, len(c), 4):
            tmp.append(c[i])
        nested.append(tmp)
    crate_d = dict()
    for i, k in enumerate(keys):
        crate_d[k] = list(filter(str.strip,[x[i] for x in nested]))
    return crate_d

def parse_instructions(instructions):
    moves = []
    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
    for i in instructions.split("\n"):
        results = pattern.findall(i)
        moves.append(results[0])
    return list(filter(None,moves))

def move_dem_crates(crate_dict, moves, reverse=True):
    for m in moves:
        origin = crate_dict[m[1]]
        if reverse is True:
            remove = list(reversed(origin[:int(m[0])]))
        else:
            remove = origin[:int(m[0])]
        new_origin = origin[int(m[0]):]
        remove.extend(crate_dict[m[2]])
        crate_dict[m[2]] = remove
        crate_dict[m[1]] = new_origin
    return "".join([v[0] for v in crate_dict.values()])
        
        
if __name__ == "__main__":
    with open("input", "r") as fh:
        crates, instructions = fh.read().split("\n\n")
    crate_dict = parse_crates(crates)
    moves = parse_instructions(instructions)
    print(move_dem_crates(crate_dict, moves, reverse=False))