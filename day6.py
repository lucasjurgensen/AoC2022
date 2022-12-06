data = open("day6.input", "r")

for line in data:
    total_idx = 4
    last_four = list(line[:4])
    for letter in line[4:]:
        if len(set(last_four)) == 4:
            print(total_idx)
            break
        idx = total_idx % 4
        last_four[idx] = letter
        total_idx = total_idx + 1

# Part 1
'''
data = open("day6.input", "r")

for line in data:
    total_idx = 4
    last_four = list(line[:4])
    for letter in line[4:]:
        if len(set(last_four)) == 4:
            print(total_idx)
            break
        idx = total_idx % 4
        last_four[idx] = letter
        total_idx = total_idx + 1
'''
