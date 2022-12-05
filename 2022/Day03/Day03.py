import string
import numpy as np

test_input="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def char2num_dict(letter):
    letter_dict = dict()
    for i, n in enumerate(string.ascii_lowercase):
        letter_dict[n] = i
    return letter_dict()

def letter2num_decode():
    letter_dict = dict()
    for i, n in enumerate(string.ascii_letters, 1):
        letter_dict[n] = i
    return letter_dict

def part1(data, letter_dict):
    total = 0
    for d in data:
        bag_size = len(d)
        compart_size = int(bag_size / 2)
        first, second = d[:compart_size], d[compart_size:]
        common = set(first).intersection(set(second))
        for c in common:
            total += letter_dict[c]
    return total

def part2(data, letter_dict):
    total = 0
    group_nums = len(data) / 3
    groups = np.array_split(data, group_nums)
    for g in groups:
        badge = set(g[0]).intersection(set(g[1]), set(g[2]))
        for b in badge:
            total += letter_dict[b]
    return total

if __name__ == "__main__":
    with open("input") as fh:
        data = fh.read().splitlines()
    letter_dict = letter2num_decode()
    print(part1(data,letter_dict))
    print(part2(data,letter_dict))