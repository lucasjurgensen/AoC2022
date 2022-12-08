data = open("day7.input", "r")
#data = open("test.input", "r")

class node():
    def __init__(self, _size=0, _name="root", _parent=None):
        self.size = _size
        self.children = {}
        self.name = _name
        self.parent = _parent if _parent else self

root = node()
curr = root

# Build up tree
for line in data:
    line = line.strip()
    contents = line.split()
    match contents[0]:
        case "$": #Function
            match contents[1]:
                case "ls":
                    pass
                case "cd":
                    if contents[2] == "/":
                        curr = root
                    elif contents[2]  == "..":
                        curr = curr.parent
                    else:
                        curr = curr.children[contents[2]]
        case "dir": #Directory
            dir_name = contents[1]
            if dir_name not in curr.children:
                curr.children[dir_name] = node(0, dir_name, curr)
        case _: #File
            file_name = contents[1]
            file_size = int(contents[0])
            if file_name not in curr.children:
                curr.children[file_name] = node(file_size, file_name, curr)

# Traverse Tree
directory_sizes_dict = {}
def calculate_directory_size(directory):
    if directory.size: 
        return directory.size
    for name, node in directory.children.items():
        if node.size:
            directory.size += node.size
        else:
            directory.size += calculate_directory_size(node)
    directory_sizes_dict[directory] = directory.size
    return directory.size


root_size = calculate_directory_size(root)
print(f"Total used size: {root_size}")
directory_size_list = sorted(list(directory_sizes_dict.items()), key=lambda x: x[1], reverse=False)

# Part 2
DEVICE_SIZE = 70000000
REQUIRED_SIZE = 30000000
remaining_space = DEVICE_SIZE - root_size
required_space = REQUIRED_SIZE - remaining_space
print(f"reuired size {required_space}")
for node in directory_size_list:
    size = node[1]
    if size > required_space:
        print(f"Part 2 Solution: {node[1]}")
        break
    

# Part 1
running_total = 0
for node in directory_size_list:
    size = node[1]
    if size > 100000:
        break
    else:
        running_total += size


print(f"Part 1 Solution: {running_total}")


