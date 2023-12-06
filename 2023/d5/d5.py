import re

test_input="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

with open("input.txt") as fh:
    test_input = fh.read()

sections = test_input.split("\n\n")
_input = list(map(int, re.findall(r"([0-9]+)", sections[0])))


# for sect in sections[1:]:
#     lines = sect.split("\n")
#     print(lines[0])
#     mapper = dict()
#     for line in lines[1:]:
#         print(line)
#         dest, source, num = map(int, line.split())
#         for i in range(num):
#             mapper[source+i] = dest+i
#     output = []       
#     for i in input:
#         output.append(mapper.get(i, i))
#     input = output[:]

# print(sorted(output)[0])

part1 = _input
for sec in sections[1:]:
    lines = sec.split("\n")
    print(lines[0])
    output = []
    mapper = []
    for line in lines[1:]:
        dest, source, num = map(int, line.split())
        mapper.append([dest, source, num-1])
    for i in part1:
        out = i
        for dest, source, num in mapper:
            if i >= source and i <= (source+num):
                diff = i - source
                out = dest + diff
        
        output.append(out)
    part1 = output

print(sorted(part1)[0])

# part 2
pairs = [ _input[i:i+2] for i in range(0, len(_input), 2)]
part2 = []

_part2 = [range(start, start+length) for start,length in pairs]

round = 1
for p in _part2:
    print(round)
    for sec in sections[1:]:
        lines = sec.split("\n")
        print(lines[0])
        output = []
        mapper = []
        for line in lines[1:]:
            dest, source, num = map(int, line.split())
            mapper.append([dest, source, num-1])
        for i in p:
            out = i
            for dest, source, num in mapper:
                if i >= source and i <= (source+num):
                    diff = i - source
                    out = dest + diff
            
            output.append(out)
        p = output
    part2.append(sorted(p)[0])
    round += 1

print(sorted(part2)[0])
    



