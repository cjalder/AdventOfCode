import regex as re

with open("input.txt") as fh:
    data = fh.read().splitlines()

part1 = []
for line in data:
    nums = re.findall(r'[1-9]', line)
    part1.append(int(f"{nums[0]}{nums[-1]}"))
print(sum(part1))

word2num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
part2 = []
for line in data:
    nums = re.findall(r'([1-9]|one|two|three|four|five|six|seven|eight|nine)', line, overlapped=True)
    nums = [word2num[i] if i in word2num else i for i in nums]
    part2.append(int(f"{nums[0]}{nums[-1]}"))
print(sum(part2))
