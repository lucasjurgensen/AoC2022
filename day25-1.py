import numpy

data = open("day25.input", "r")

total_value = 0

for line in data:
    line = list(line.strip())
    value = 0
    power = 0
    while line:
        dig = line.pop()
        match dig: 
            case "-":
                dig = -1
            case "=":
                dig = -2
            case _:
                dig = int(dig)
        value +=  pow(5, power) * dig
        power += 1
    total_value += value
    print(value)

print(f"Total Value: {total_value}")

total_valye_b5 = str(numpy.base_repr(total_value, base=5))
tv5 = ["0"] + list(str(total_valye_b5))
for idx in range(len(tv5)-1, -1, -1):
    print(idx)
    char = tv5[idx]
    match char:
        case "0":
            continue
        case "1":
            continue
        case "2":
            continue
        case "3":
            tv5[idx] = "="
            tv5[idx-1] = str(int(tv5[idx-1]) + 1)
        case "4":
            tv5[idx] = "-"
            tv5[idx-1] = str(int(tv5[idx-1]) + 1)
        case "5":
            tv5[idx] = "0"
            tv5[idx-1] = str(int(tv5[idx-1]) + 1)

if tv5[0] == "0":
    tv5 = tv5[1:]
tv5 = "".join(tv5)
print(f"Snafu total: {tv5}")



# Slow way of manually building up the value
def slow_solution():
    global snafu_final
    memo = {}
    def add_one(snafu_num):
        if not snafu_num:
            return "1"

        last_dig = snafu_num[-1]
        rest = snafu_num[:-1]
        match last_dig:
            case "1":
                return rest + "2"
            case "2":
                return add_one(rest) + "="
            case "=":
                return rest + "-"
            case "-":
                return rest + "0"
            case "0":
                return rest + "1"
            


    snafu_final = "0"
    for i in range(6103515625):
        snafu_final = add_one(snafu_final)

        

    print(f"Snafu final: {snafu_final}")

