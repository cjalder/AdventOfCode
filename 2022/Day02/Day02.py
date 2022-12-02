test_input = """A Y
B X
C Z"""




def outcome_score(a,b):
    out_dict = {"A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3}}
    return out_dict[a][b]

def shape_score(b):
    shape = {"X": 1, "Y": 2, "Z": 3}
    return shape[b]

def fixing(b):
    fix_dict = {"X": 0, "Y": 3, "Z": 6}
    return fix_dict[b]

def shape_fixing(a,b):
    fix_choice = {"A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1}}
    return fix_choice[a][b]

def part1(rounds):
    total_score = 0
    for round in rounds:
        them, you = round.split()
        shape = shape_score(you)
        outcome = outcome_score(them, you)
        rnd_score = shape + outcome
        total_score += rnd_score
    return total_score  



def part2(rounds):
    fixed_score = 0
    for round in rounds:
        them, you = round.split()
        fix = fixing(you)
        shape = shape_fixing(them,you)
        # print(fix, shape)
        rnd_score = fix + shape
        fixed_score += rnd_score
    return fixed_score




if __name__ == "__main__":
    # rounds = test_input.split("\n")
    with open("input", "r") as fh:
        round_input = fh.read().splitlines()
    print(part1(round_input))
    print(part2(round_input))
