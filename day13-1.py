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

def compare(pair):
    # x is value of first, y is value of second
    second = pair[1]
    for x in pair[0]:
        if not second:
            return False
        y = second.pop(0)

        if type(x) == list or type(y) == list:
            res = compare([listify(x), listify(y)])
            if res != None:
                print("here with res")
                return res

        elif x > y:
            return False
        elif y > x:
            return True

    if second:
        return True
    return None

result = []
pair = []
for idx, line in enumerate(data):
    line = line.strip()
    if line:
        pair.append(parse(list(line)[1:]))
    else:
        comp = compare(pair)
        if comp:
            result.append(int((1 + (idx-2)/3)))
        pair = []

print(f"Result = {sum(result)}", result)