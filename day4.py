data = open("day4.input", 'r')

overlapping_pairs = 0
total = 0
for idx, pair in enumerate(data):
    pair = [list(map(int,x.split('-'))) for x in list(pair.strip().split(','))]
    if pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]:
        overlapping_pairs += 1 # Elf 0 start is within elf 1
    elif pair[0][1] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        overlapping_pairs += 1 # Elf 0 end is within elf 1
    elif pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        overlapping_pairs += 1 # Elf 1 is fully within elf 0

print(overlapping_pairs, total)


# Part 1
'''
data = open("day4.input", 'r')

overlapping_pairs = 0
total = 0
for idx, pair in enumerate(data):
    pair = [list(map(int,x.split('-'))) for x in list(pair.strip().split(','))]
    # If elf 0 contains elf1
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        overlapping_pairs += 1
    # If elf 1 contains elf 0
    elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
        overlapping_pairs += 1
print(overlapping_pairs, total)
'''
