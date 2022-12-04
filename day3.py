data = open("day3.input","r")

total_priority = 0


def get_value(char):
    if char >= 'a' and char <= 'z':
        return (ord(char) - 96)
    if char >= 'A' and char <= 'Z':
        return (ord(char) - 38)
    else:
        raise Exception("not an expected character")

group = []
for ruck in data:
    group.append(ruck.strip())
    if len(group) < 3:
        continue
    char_set = set(list(group[0]))
    char_sub_set = set({})
    for char in group[1]:
        if (char in char_set): 
            char_sub_set.add(char)
    for char in group[2]:
        if char in char_sub_set:
            total_priority += get_value(char)   
            group = []
            break
print(total_priority)


# Part 1
'''
data = open("day3.input","r")

total_priority = 0


def get_value(char):
    if char >= 'a' and char <= 'z':
        return (ord(char) - 96)
    if char >= 'A' and char <= 'Z':
        return (ord(char) - 38)
    else:
        raise Exception("not an expected character")

for ruck in data:
    ruck = ruck.strip()
    split = int(len(ruck)/2)
    char_set = set({})
    for char in ruck[:split]:
        char_set.add(char)
    for char in ruck[split:]:
        if char in char_set:
            total_priority += get_value(char)
            print(ruck, char_set, char)
            break

print(get_value('a'), get_value('z'), get_value('A'), get_value('Z'))
print(total_priority)
'''
