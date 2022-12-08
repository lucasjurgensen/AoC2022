data = open("day8.input", "r")
#data = open("test.input", "r")

matrix = []
for line in data:
    matrix.append(line.strip())

num_rows = len(matrix)
num_columns = len(matrix[0])

# Part 2 #
max_tree_score = -1
for row in range(num_rows):
    for column in range(num_columns):
        tree_height = matrix[row][column]
        tree_score = 1
        # going down
        multiplier = 0
        for down_row in range(row+1, num_rows):
            multiplier += 1
            if tree_height <= matrix[down_row][column]:
                break
        tree_score *= multiplier
        # going up
        multiplier = 0
        for up_row in range(row-1, -1, -1):
            multiplier +=1
            if tree_height <= matrix[up_row][column]:
                break
        tree_score *= multiplier
        # going right
        multiplier = 0
        for right_column in range(column+1, num_columns):
            multiplier += 1
            if tree_height <= matrix[row][right_column]:
                break
        tree_score *= multiplier
        # going left
        multiplier = 0
        for left_column in range(column-1, -1, -1):
            multiplier += 1
            if tree_height <= matrix[row][left_column]:
                break
        tree_score *= multiplier
        max_tree_score = max(tree_score, max_tree_score)

print(f"Part 2 Solutin {max_tree_score}")

# Part 1 #
visible_trees = set({})
# Down the rows, across the columns
for row in range(0, num_rows):
    tree_line = [-1]
    for column in range(0, num_columns):
        tree_height = int(matrix[row][column])
        if tree_height > tree_line[-1]:
            tree_line.append(tree_height)
            visible_trees.add((row, column)) 

# Down the rows, back across the columns
for row in range(0, num_rows):
    tree_line = [-1]
    for column in range(num_columns-1, -1, -1):
        tree_height = int(matrix[row][column])
        if tree_height > tree_line[-1]:
            tree_line.append(tree_height)
            visible_trees.add((row, column))

# Across the columns, down the rows
for column in range(0, num_columns):
    tree_line = [-1]
    for row in range(0, num_rows):
        tree_height = int(matrix[row][column])
        if tree_height > tree_line[-1]:
            tree_line.append(tree_height)
            visible_trees.add((row,column))

# Across the columns, up the rows
for column in range(0, num_columns):
    tree_line = [-1]
    for row in range(num_rows-1, -1, -1):
        tree_height = int(matrix[row][column])
        if tree_height > tree_line[-1]:
            tree_line.append(tree_height)
            visible_trees.add((row,column))

print(f"Part 1 Solution: {len(visible_trees)}")


def visualize():
    result_map = []
    for i in range(num_columns):
        result_map.append([0]*num_rows)

    iterations = 0  
    for pair in visible_trees:
        result_map[pair[0]][pair[1]] = 1

    for res in result_map:
        print(res)

#visualize()
