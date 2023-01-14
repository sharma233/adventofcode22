import re

# name: str
# parent: 'FS_Node'
# children: list['FS_Node']
# size: float

class FS_Node:
    def __init__(self, name, parent=None, children=[], size=0):
        self.name = name
        self.parent = parent
        self.children = children
        self.size = size

def build_dir_structure() -> FS_Node:
    current_node:FS_Node = FS_Node("placeholder")
    parent_node = current_node

    with open("inputs/day7/real.txt", "r") as problem_input:
        line = problem_input.readline()
        while(line):
            if "cd" in line:
                fs_object_name = line[5:].strip()
                if(fs_object_name == ".."):
                    current_node = current_node.parent
                else:
                    found = False
                    for child in current_node.children:
                        if child.name == fs_object_name:
                            current_node = child
                            found = True
                    if not found:
                        new_node = FS_Node(fs_object_name, current_node, [], 0)
                        current_node.children.append(new_node)
                        current_node = new_node
                line = problem_input.readline()
            elif "ls" in line:
                line = problem_input.readline()
                while line and line.startswith("$") == False:
                    new_node = None
                    file_parts = line.split()
                    if(file_parts[0] == "dir"):
                        new_node = FS_Node(file_parts[1], current_node, [], 0)
                    else:
                        new_node = FS_Node(file_parts[1], current_node, [], int(file_parts[0]))

                    current_node.children.append(new_node)
                    line = problem_input.readline()
    return parent_node.children[0] #first child should always just be the root dir

def calculate_dir_sizes(root_node: FS_Node):
    if len(root_node.children) == 0:
        return root_node.size

    total = 0
    for child in root_node.children:
        total += calculate_dir_sizes(child)
    root_node.size = total
    return total 

def return_total_size_of_dirs_less_than_size(root_node, size, total):
    if(len(root_node.children) == 0):
        return total
    for child in root_node.children:
        total = return_total_size_of_dirs_less_than_size(child, size, total)
    if root_node.size <= size:
        return total + root_node.size
    
    return total

TOTAL_SPACE = 70000000
def find_smallest_possible_dir(root_node, candidate_node, target):
    if(len(candidate_node.children) == 0):
        return candidate_node
    
    for child in root_node.children:
        candidate_node = find_smallest_possible_dir(child, candidate_node, target)

    if(root_node.size < target):
        return candidate_node

    if(root_node.size <= candidate_node.size and len(root_node.children) > 0):
        return root_node

    return candidate_node

root_node = build_dir_structure()
calculate_dir_sizes(root_node)
print("PART 1: ")
print(return_total_size_of_dirs_less_than_size(root_node, 100000, 0))
print("PART 2: ")
current_free_space = TOTAL_SPACE - root_node.size
print(find_smallest_possible_dir(root_node, root_node, 30000000-current_free_space).size)