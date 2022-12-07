from collections import defaultdict
test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def change(_current, cmd, _tree):
    if cmd == "..":
        target = _tree[current]["parent"]
    else:
        target = cmd
    return target


# print(test_input.split("$"))

data = [i.split() for i in test_input.split("\n")]
# with open("input", "r") as fh:
#     data = [i.split() for i in fh.read().splitlines()]
export = False
current = None
tree = dict()
for d in data:
    if d[0] == "$":
        if d[1] == "cd":
            if current and export:
                tree[current].update({"files": f_list, "child": d_list})
                export = False
            new_dir = change(current, d[2], tree)
            if new_dir not in tree.keys():
                tree[new_dir] = {"parent": current}
                current = new_dir
        if d[1] == "ls":
            export = True
            f_list = []
            d_list = []
    else:
        if d[0] == "dir":
            d_list.append(d[1])
        else:
            f_list.append(int(d[0]))
tree[current].update({"files": f_list, "child": d_list})

LIMIT = 100000
# for k in tree.keys():
#     KEEP = True
#     total = 0
#     current = k
#     while KEEP:
#         files = tree[current]["files"]
#         total += sum(files)
#         sub = tree[current]["child"]
#         if len(sub) == 0:
#             KEEP = False
#         else:
#             current = 
#     print(k, total)

def dir_size(tree, current, size=0):
    childs = tree[current]["child"]
    size += sum(tree[current]["files"])
    if len(childs) == 0:
        return size
    else:
        for c in childs:
            return dir_size(tree,c,size)

part1 = 0
for k in tree.keys():
    total = dir_size(tree, k)
    if total <= LIMIT:
        part1 += total

print(part1)

