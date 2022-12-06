from itertools import islice
test_input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

with open("input", "r") as fh:
    data = fh.read().strip()

def find_first_uniq(code, k):
    for i, n in enumerate(range(k,len(code))):
        if len(set(code[i:n])) == k:
            return n

print(f"Part 1: {find_first_uniq(data,4)}")    
print(f"Part 2: {find_first_uniq(data,14)}")