import heapq

from load_input import get_aoc_input

raw = get_aoc_input(2022, 1)
calories = [sum([int(c.strip()) for c in elf.split('\n')]) for elf in raw.strip().split('\n\n')]

print('Part 1:', max(calories))
print('Part 2:', sum(heapq.nlargest(3, calories)))
