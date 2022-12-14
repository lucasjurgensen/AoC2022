import inspect
import time

data = open("day11.input", "r")
#data = open("test.input", "r")

class monkey():
    items = None
    raw_operation = None
    operand = None

    test_divisor = None
    next_on_true = None
    next_on_false = None
    def __init__(self, num):
        self.num = num
    
    def inspect(self, old):
        return self.raw_operation(old, self.operand)        

    def __str__(self):
        return(f"monkey {self.num} has {self.items}") 

current_monkey = None
monkey_list = []

for line in data:
    contents = line.strip().split()
    if not contents:
        monkey_list.append(current_monkey)
        continue

    match contents[0], contents[1]:
        case "Monkey", _:
            current_monkey = monkey(contents[1].strip(":"))
        case "Starting", _:
            current_monkey.items = [int(x.strip(',')) for x in contents[2:]]
        case "Operation:", _:
            operator = contents[4]
            match operator, contents[5]:
                case "*", "old":
                    current_monkey.raw_operation = (lambda old, oper : pow(old, 2))
                    current_monkey.operand = None
                case "*", _:
                    current_monkey.raw_operation = (lambda old, oper: old * oper)
                    current_monkey.operand = int(contents[5])
    
                case "+", "old": 
                    current_monkey.raw_aperation = (lambda old, oper: old + old)
                    current_monkey.operand = None
                case "+", _:
                    current_monkey.raw_operation = (lambda old, oper: old + oper)
                    current_monkey.operand = int(contents[5])

        case "Test:", _:
            current_monkey.test_divisor = int(contents[3])
        
        case "If", "true:":
            current_monkey.next_on_true = int(contents[5])
        case "If", "false:":
            current_monkey.next_on_false = int(contents[5])

for monkey in monkey_list:
    print(monkey)

print("Starting \n")

monkey_inspections = {}
max_worry = 1
for monkey_num in range(len(monkey_list)):
    monkey_inspections[monkey_num] = 0    
    max_worry *= monkey_list[monkey_num].test_divisor

for round in range(10000):
    print(round)
    for monkey in monkey_list:
        while monkey.items:
            # Monkey inspects
            monkey.items[0] = monkey.inspect(monkey.items[0])
            monkey_inspections[int(monkey.num)] += 1
            # Monkey gets bored
            #monkey.items[0] = monkey.items[0] // 3         # Use for part 1
            monkey.items[0] = monkey.items[0] % max_worry   # Use for part 2
            # Monkey passes
            if monkey.items[0] % monkey.test_divisor:
                monkey_list[monkey.next_on_false].items.append(monkey.items.pop(0))
            else:
                monkey_list[monkey.next_on_true].items.append(monkey.items.pop(0))

print(monkey_inspections)

print(sorted(monkey_inspections.items(), key = lambda item: item[1]))
