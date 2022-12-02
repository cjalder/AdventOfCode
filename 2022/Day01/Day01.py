
test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def fattest_elf(input: str) -> int:
    fattest = 0
    data = input.split("\n\n")
    for line in data:
        count = 0
        for l in line.split():
            count += int(l)
        if count > fattest:
            fattest = count
    return fattest

def fattest_trio(input):
    fat_list = []
    data = input.split("\n\n")
    for line in data:
        count = 0
        for l in line.split():
            count += int(l)
        fat_list.append(count)
    fat_list = sorted(fat_list, reverse=True)
    return sum(fat_list[:3])  


def part1():
    test = fattest_elf(test_input)
    print(f"Fattest elf for test: {test}")
    with open("input", "r") as fh:
        p1_input = fh.read()
    p1_ans = fattest_elf(p1_input)
    print(f"Fattest elf for part 1: {p1_ans}")

def part2():
    test = fattest_trio(test_input)
    print(f"Fattest trio for test: {test}")
    with open("input", "r") as fh:
       p1_input = fh.read()
    p1_ans = fattest_trio(p1_input)
    print(f"Fattest trio for part 1: {p1_ans}")

if __name__ == "__main__":
    part2()



