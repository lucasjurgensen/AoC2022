import math

data = open("day5.input", "r")

building_stacks = True
stacks_data = []
stacks = []
for line in data:
    line = line.strip("\n")

    # First input data into list of stacks
    if building_stacks:
        if line == "":
            building_stacks = False
            num_stacks = math.ceil(len(stacks_data.pop()) / 4)
            idx = 1
            for stack in range(num_stacks):
                curr_stack = []
                for box in range(len(stacks_data)-1, -1, -1):
                    if stacks_data[box][idx] != ' ':
                        curr_stack.append(stacks_data[box][idx])
                    else:
                        break
                stacks.append(curr_stack)
                idx += 4
                    
        else:
            stacks_data.append(line)
    
    # Now, calculate the individual moves
    else: # moving
        move = line.split(' ')
        quant, source, dest = int(move[1]), int(move[3])-1, int(move[5])-1
        quant = min(quant, len(stacks[source]))

        tmp = []
        for i in range(quant):
            tmp.append(stacks[source].pop())
        tmp.reverse()
        stacks[dest] += tmp    

tops = []
for stack in stacks:
    tops.append(stack.pop())

print(''.join(tops))



# Part 1
'''
import math

data = open("day5.input", "r")

building_stacks = True
stacks_data = []
stacks = []
for line in data:
    line = line.strip("\n")

    # First input data into list of stacks
    if building_stacks:
        if line == "":
            building_stacks = False
            num_stacks = math.ceil(len(stacks_data.pop()) / 4)
            idx = 1
            for stack in range(num_stacks):
                curr_stack = []
                for box in range(len(stacks_data)-1, -1, -1):
                    if stacks_data[box][idx] != ' ':
                        curr_stack.append(stacks_data[box][idx])
                    else:
                        break
                stacks.append(curr_stack)
                idx += 4
                    
        else:
            stacks_data.append(line)
    
    # Now, calculate the individual moves
    else: # moving
        move = line.split(' ')
        quant, source, dest = int(move[1]), int(move[3])-1, int(move[5])-1
        for i in range(quant):
            if not stacks[source]:
                break
            stacks[dest].append(stacks[source].pop())
    
tops = []
for stack in stacks:
    tops.append(stack.pop())

print(''.join(tops))
'''
