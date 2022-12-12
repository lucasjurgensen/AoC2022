data = open("day9.input", "r")
#data = open("test.input", "r")

knots = [[0,0] for _ in range(10)]
tail_visits = {(0,0)}
for move in data:
    contents = move.split()
    direction = contents[0]
    steps = int(contents[1])
    while steps:
        # Move Head
        match direction:
            case "U":
                knots[0][1] += 1
            case "R":
                knots[0][0] += 1
            case "D":
                knots[0][1] -= 1
            case "L":
                knots[0][0] -= 1

        # Move rest
        for i in range(1, 10):
            delta_x = knots[i-1][0] - knots[i][0]
            delta_y = knots[i-1][1] - knots[i][1]
            x_dir = int(abs(delta_x) / delta_x if delta_x else 0)
            y_dir = int(abs(delta_y) / delta_y if delta_y else 0)

            if abs(delta_x) > 1:
                knots[i][0] += x_dir
                if delta_y:
                    knots[i][1] += y_dir

            elif abs(delta_y)  > 1:
                knots[i][1] += y_dir
                if delta_x:
                    knots[i][0] += x_dir

            else:
                break

            # Track tail movement
            if i == 9:
                tail_visits.add((knots[i][0], knots[i][1]))
        steps -= 1

print(tail_visits)
print(len(tail_visits))



# Part 1
'''
head = [0,0]
tail = [0,0]
tail_visits = {(0,0)}
for move in data:
    contents = move.split()
    direction = contents[0]
    steps = int(contents[1])
    while steps:
        # Move Head
        match direction:
            case "U":
                head[1] += 1
            case "R":
                head[0] += 1
            case "D":
                head[1] -= 1
            case "L":
                head[0] -= 1
        # Move Tail
        delta_x = head[0] - tail[0]
        delta_y = head[1] - tail[1]
        x_dir = int(abs(delta_x) / delta_x if delta_x else 0)
        y_dir = int(abs(delta_y) / delta_y if delta_y else 0)

        if abs(delta_x) > 1:
            tail[0] += x_dir
            if delta_y:
                tail[1] += y_dir
            tail_visits.add((tail[0], tail[1]))

        elif abs(delta_y)  > 1:
            tail[1] += y_dir
            if delta_x:
                tail[0] += x_dir
            tail_visits.add((tail[0], tail[1]))

        else:
            pass
            
        steps -= 1
print(tail_visits)
print(len(tail_visits))
'''
