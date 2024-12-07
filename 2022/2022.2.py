from load_input import get_aoc_input
from itertools import permutations

raw = get_aoc_input(2022, 2)

abc = ['A', 'B', 'C']
scores = {shape: i+1 for i, shape in enumerate(abc)}
match_ups = {mu: 0 for mu in permutations(abc, 2)}
for draw in zip(abc, abc):
    match_ups[draw] = -1
for right_win in [('A', 'B'), ('B', 'C'), ('C', 'A')]:
    match_ups[right_win] = 1

xyz_map = {a: b for a, b in zip(['X', 'Y', 'Z'], abc)}

score = 0
for left, right in [round.split(' ') for round in raw.strip().split('\n')]:
    right = xyz_map[right]
    match match_ups[(left, right)]:
        case -1:  # draw
            score += 3
        case 0:
            score += 0
        case 1:
            score += 6
    score += scores[right]

print('Part 1:', score)
