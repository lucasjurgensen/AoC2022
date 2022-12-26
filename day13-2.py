from functools import cmp_to_key

data = open("day13.input", "r")

def parse(line_arr):
    arr = []
    while line_arr:
        char = line_arr.pop(0)
        match char:
            case "[":
                arr.append(parse(line_arr))
            case "]":
                return arr
            case ",":
                pass
            case _:
                # If the next char is also a digit, lump them together
                if line_arr[0] >= '0' and line_arr[0] <= '9':
                    line_arr[0] += str(int(char) * 10)
                else:
                    arr.append(int(char))
    return arr

def listify(x):
    # Funciton needed so that we can wrap ints in lists
    if type(x) == int:
        return [x]
    else:
        return list(x)

def compare(first, second):
    # x is value of first, y is value of second
    for x in first:
        if not second:
            return -1
        y = second.pop(0)

        if type(x) == list or type(y) == list:
            res = compare(listify(x), listify(y))
            if res != 0:
                return res

        elif x > y:
            return -1
        elif y > x:
            return 1

    if second:
        return 1

    return 0

aggregated = [[[2]],[[6]]]
for idx, line in enumerate(data):
    line = line.strip()
    if line:
        adding = parse(list(line)[1:])
        aggregated.append(adding)
    else:
        continue

# Bubble Sort!
working = True
while working:
    changed = False
    for x in range(len(aggregated)-1):
        comp_res = compare(aggregated[x][:], aggregated[x+1][:])
        if comp_res < 0:
            changed = True
            aggregated[x], aggregated[x+1] = aggregated[x+1], aggregated[x]
    if not changed:
        break

for agg in aggregated:
    print(agg)

print((aggregated.index([[2]])+1) * (aggregated.index([[6]])+1))
