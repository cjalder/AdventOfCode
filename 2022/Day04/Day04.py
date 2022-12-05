test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def main(data):
    part1 = 0
    part2 = 0
    for i in data:
        m ,n = [[int(x) for x in j.split("-")] for j in i.split(",")]
        elf1 = set(range(m[0], m[1]+1))
        elf2 = set(range(n[0], n[1]+1))
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            part1 += 1
        if len(elf1.intersection(elf2)) >= 1:
            part2 += 1    
    return part1, part2



if __name__ == "__main__":
    with open("input", "r") as fh:
        data = fh.read().splitlines()
    print(main(data))