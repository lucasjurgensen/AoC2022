import pdb
import re

f = open("day1.input", "r")

current_tally = 0
number_of_max = 3
max_tally = [0]*number_of_max
for line in f:
    if not re.search("\d+", line):
        for idx, mx in enumerate(max_tally):
            if current_tally > mx:
                max_tally[idx] = current_tally
                max_tally.sort()
                break
        current_tally = 0
    else:
        current_tally += int(line)

print(max_tally)
print(sum(max_tally))


# Part 1
"""
import pdb
import re

f = open("day1.input", "r")

current_tally = 0
max_tally = 0
for line in f:
    if not re.search("\d+", line):
        if current_tally > max_tally:
            max_tally = current_tally
        current_tally = 0
    else:
        current_tally += int(line)

print(max_tally)
"""
