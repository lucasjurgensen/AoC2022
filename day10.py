data = open("day10.input", "r")

cycle = 1
register_x = 1

SCREEN_WIDTH = 40
SCREEN_PIXELS = 240

screen = [0] * SCREEN_PIXELS

def draw():
    global cycle, screen
    if (cycle-1) % SCREEN_WIDTH in list(range(register_x-1,register_x+2)):
        screen[cycle-1] = '#'
    else:
        screen[cycle-1] = '.'

def print_screen():
    global screen
    for i in range(int(SCREEN_PIXELS/SCREEN_WIDTH)):
        start = i * SCREEN_WIDTH
        end = (i+1) * SCREEN_WIDTH
        print("".join(screen[start:end]))

for line in data:
    contents = line.strip().split()
    match contents[0]:
        case "noop":
            draw()
            cycle += 1
        case "addx":
            draw()
            cycle += 1        
            draw()
            register_x += int(contents[1])
            cycle += 1

print_screen()


# Part 1
'''
cycle = 1
register_x = 1
important_cycles = [20,60,100,140,180,220]

signal_strength = 0

def measure_strength():
    global signal_strength
    if important_cycles and cycle == important_cycles[0]:
        signal_strength += important_cycles.pop(0) * register_x

for line in data:
    contents = line.strip().split()
    match contents[0]:
        case "noop":
            # does nothing
            cycle += 1
            measure_strength()
        case "addx":
            cycle += 1        
            measure_strength()
            cycle += 1
            register_x += int(contents[1])
            measure_strength()    

print(signal_strength)            
'''
