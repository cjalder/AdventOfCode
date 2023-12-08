from collections import Counter, OrderedDict
test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

with open("input.txt") as fh:
    test_input = fh.read()

card_rank = {"A":13, "K":12, "Q":11, "J":10, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}

def hand_type(hand):
    rank = {
        (5,0): "fivekind",
        (4,1): "fourkind",
        (3,2): "fullhouse",
        (3,1): "threekind",
        (2,2): "twopair",
        (2,1): "onepair",
        (1,1): "high"
        }
    counts = Counter(hand).most_common()
    if len(counts) == 1:
        return rank[(5,0)]
    else:
        return rank[(counts[0][1], counts[1][1])]
    
    

games = dict()
for line in test_input.splitlines():
    hand, bet = line.split()
    games[hand] = {"bet": int(bet), "res": hand_type(hand)}

order = ["high", "onepair", "twopair", "threekind", "fullhouse", "fourkind", "fivekind"]

part1 = []
rank = 1
for o in order:
    h_type = {k:v for k,v in games.items() if v["res"] == o}
    if h_type:
        ranks = {tuple(card_rank[i] for i in k):k for k in h_type.keys()}
        for k, v in sorted(ranks.items()):
            part1.append(h_type[v]["bet"] * rank)
            rank += 1

print(sum(part1))

### Part2

card_rank = {"A":13, "K":12, "Q":11, "J":1, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}

def hand_type_joker(hand):
    rank = {
        (5,0): "fivekind",
        (4,1): "fourkind",
        (3,2): "fullhouse",
        (3,1): "threekind",
        (2,2): "twopair",
        (2,1): "onepair",
        (1,1): "high"
        }
    counts = Counter(hand)
    joker = counts.pop("J",0)
    if joker == 5:
        return rank[(5,0)]
    for k, v in counts.most_common():
        if v + joker <= 5:
            counts[k] += joker
            break
    counts = counts.most_common()
    if len(counts) == 1:
        return rank[(5,0)]
    return rank[(counts[0][1], counts[1][1])]

games = dict()
for line in test_input.splitlines():
    hand, bet = line.split()
    games[hand] = {"bet": int(bet), "res": hand_type_joker(hand)}

order = ["high", "onepair", "twopair", "threekind", "fullhouse", "fourkind", "fivekind"]

part2 = []
rank = 1
for o in order:
    h_type = {k:v for k,v in games.items() if v["res"] == o}
    print(h_type)
    if h_type:
        ranks = {tuple(card_rank[i] for i in k):k for k in h_type.keys()}
        for k, v in sorted(ranks.items()):
            print(v)
            part2.append(h_type[v]["bet"] * rank)
            rank += 1

print(sum(part2))

    
    



# for game, bet in games:
#     print(Counter(game))
#     pairs = (len(set(game)) - len(game)) % 2
#     print(pairs)