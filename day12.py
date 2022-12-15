# Part 2
data = open("day12.input", "r")

matrix = []
for line in data:
    matrix.append(list(line.strip()))

def find(x):
    global matrix
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == x:
                return(row, column)

# Find start and end positions
start_x, start_y = find("E")

# Initiate dictionary of visited and queue of to visit
visits = {(start_x, start_y)} # of form (x,y)
adjacents = [("E", (start_x, start_y), 0, [])] # of form (letter, (x,y), dist, [path])
prev_matrix = [[None]*len(matrix[0]) for x in range(len(matrix))]

# For algo, replace start and end with heights
old_start_x, old_start_y = find("S")
matrix[old_start_x][old_start_y] = "a"
matrix[start_x][start_y] = "z"


def calculate_path(x, y):
    """Prints the path from desination to start"""
    global start_x, start_y
    print(x,y)
    if x == start_x and y == start_y:
        return
    prev_x, prev_y = prev_matrix[x][y]
    calculate_path(prev_x, prev_y)

# Loop which performs djikstra's to find shortest path
while True:
    # explore from head
    head = adjacents.pop(0)
    print(f"at {head}")
    head_x = head[1][0]
    head_y = head[1][1]
    head_letter = head[0]
    head_distance = head[2]
    if head_letter == "a":
        print(f"Nearest 'a' is {head_distance} from the start")
        #calculate_path(head_x, head_y)
        break
    # add new adjacents (spot, distance)
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        x, y = head_x + dx, head_y + dy
        if x >= len(matrix) or x < 0 or y >= len(matrix[0]) or y < 0:
            # skip if out of bounds
            continue
        if (x,y) not in visits:
            if ord(matrix[x][y]) >= ord(matrix[head_x][head_y])-1:
                visits.add((x,y))
                adjacents.append((matrix[x][y], (x,y), head_distance + 1))
                prev_matrix[x][y] = (head_x, head_y)

# Part 1
"""
data = open("day12.input", "r")

matrix = []
for line in data:
    matrix.append(list(line.strip()))

def find(x):
    global matrix
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == x:
                return(row, column)

# Find start and end positions
start_x, start_y = find("S")
end_x, end_y = find("E")

# Initiate dictionary of visited and queue of to visit
visits = {(start_x, start_y)} # of form (x,y)
adjacents = [("S", (start_x, start_y), 0, [])] # of form (letter, (x,y), dist, [path])
prev_matrix = [[None]*len(matrix[0]) for x in range(len(matrix))]

# For algo, replace start and end with heights
matrix[start_x][start_y] = "a"
matrix[end_x][end_y] = "z"


def calculate_path(x, y):
    #Prints the path from desination to start
    global start_x, start_y
    print(x,y)
    if x == start_x and y == start_y:
        return
    prev_x, prev_y = prev_matrix[x][y]
    calculate_path(prev_x, prev_y)

# Loop which performs djikstra's to find shortest path
while True:
    # explore from head
    head = adjacents.pop(0)
    print(f"at {head}")
    head_x = head[1][0]
    head_y = head[1][1]
    head_letter = head[0]
    head_distance = head[2]
    if head_x == end_x and head_y == end_y:
        print(f"'E' is {head_distance} from the start")
        #calculate_path(head_x, head_y)
        break
    # add new adjacents (spot, distance)
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        x, y = head_x + dx, head_y + dy
        if x >= len(matrix) or x < 0 or if y >= len(matrix[0]) or y < 0:
            # Skip if out of bounds
            continue
        if (x,y) not in visits:
            if ord(matrix[x][y]) <= ord(matrix[head_x][head_y])+1:
                visits.add((x,y))
                adjacents.append((matrix[x][y], (x,y), head_distance + 1))
                prev_matrix[x][y] = (head_x, head_y)
"""
