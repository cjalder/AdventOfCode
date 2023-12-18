test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

with open("input.txt") as fh:
    test_input = fh.read().strip()


part1 = []
for code in test_input.split(","): 
    current = 0
    for c in code:
        current += ord(c)
        current *= 17
        current = current % 256
    part1.append(current)

print(sum(part1))

import re 
part2 = dict()
for code in test_input.split(","):
    if "=" in code:
        label, focal = code.split("=")
        box = (label, focal)
        remove = False
    else:
        label, _ = code.split("-")
        remove = True
    current = 0
    for l in label:
        current += ord(l)
        current *= 17
        current = current % 256
    if current not in part2:
        part2[current] = []
    if part2[current]:
        labels = [x for x,y in part2[current]]
        if label in labels:
            position = labels.index(label)
            del part2[current][position]
            if remove is False:
                part2[current].insert(position, box)
        elif remove is False:
            part2[current].append(box)
    elif remove is False:
        part2[current].append(box)
ans = 0
for box, lenses in part2.items():
    if lenses is None:
        continue
    for i, (lens, focal) in enumerate(lenses, start=1):
        ans += (box+1) * int(focal) * i

print(ans)



    



