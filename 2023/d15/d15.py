from collections import defaultdict
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

part2 = defaultdict(dict)
for code in test_input.split(","):
    if "=" in code:
        label, focal = code.split("=")
        remove = False
    else:
        label, _ = code.split("-")
        remove = True
    current = 0
    for l in label:
        current += ord(l)
        current *= 17
        current = current % 256
    if remove is False:
        part2[current][label] = int(focal)
    else:
        if label in part2[current]:
            part2[current].pop(label)

ans = 0
for box, lenses in part2.items():
    if lenses is None:
        continue
    for i, focal in enumerate(lenses.values(), start=1):
        ans += (box+1) * focal * i

print(ans)



    



