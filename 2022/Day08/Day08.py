import numpy as np
test_input = """30373
25512
65332
33549
35390"""


# data = [[int(i) for i in t] for t in test_input.split("\n")]
with open("input", "r") as fh:
    data = fh.read().splitlines()

# perimeter
part1 = (len(data) * 2) + (len(data) * 2) - 4
# bottom = data[-1]
# left = [d[0] for d in data]
# right = [d[-1] for d in data]

part2 = 0
#top to bottom
for i in range(1,len(data[0])-1):
    #left to right
    for j in range(1,len(data)-1):
        pos = data[i][j]
        top = [d[j] for d in data[:i]]
        bottom = [d[j] for d in data[i+1:]]
        left = data[i][:j]
        right = data[i][j+1:]
        #part1
        if pos > max(left) or pos > max(right) or pos > max(top) or pos > max(bottom):
            part1 += 1
        # part2
        scene_score = []
        left_idx = [idx for idx, x in enumerate(left) if x >= pos]
        if len(left_idx) == 0:
            scene_score.append(j)
        else:
            scene_score.append(j-left_idx[-1])
        right_idx = [idx for idx, x in enumerate(right) if x >= pos]
        if len(right_idx) == 0:
            scene_score.append(len(data[i]) - j - 1)
        else:
            scene_score.append(right_idx[0] + 1)
        top_idx = [idx for idx, x in enumerate(top) if x >= pos]
        if len(top_idx) == 0:
            scene_score.append(i)
        else:
            scene_score.append(i-top_idx[-1])
        bottom_idx = [idx for idx, x in enumerate(bottom) if x >= pos]
        if len(bottom_idx) == 0:
            scene_score.append(len(data) - i - 1)
        else:
            scene_score.append(bottom_idx[0] + 1)
        scenic_total = np.prod(scene_score)
        if scenic_total > part2:
            part2 = scenic_total

print(part1)
print(part2)
        
        
        
