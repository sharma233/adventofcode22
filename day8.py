grid = []
def build_grid():
    with open("inputs/day8/real.txt", "r") as problem_input:
        for line in problem_input:
            line_trees = []
            for char in line.strip():
                line_trees.append(int(char))
            grid.append(line_trees)

build_grid()
GRID_MAX_X = len(grid[0])
GRID_MAX_Y = len(grid)

def calculate_visible_trees():
    visible_trees = 0
    for idx_y, row in enumerate(grid):
        for idx_x, _ in enumerate(row):
            if visible(idx_x, idx_y):
                visible_trees += 1
    return visible_trees

def best_scenic_score():
    best_score = 0
    for idx_y, row in enumerate(grid):
        for idx_x, _ in enumerate(row):
            current_score = calculate_scenic_score(idx_x, idx_y)
            if current_score > best_score:
                best_score = current_score
    return best_score

def visible(idx_x, idx_y):
    #if boundary tree, return true
    if(idx_x == 0 or idx_x == (GRID_MAX_X-1) or idx_y == 0 or idx_y == (GRID_MAX_Y-1)):
        return True

    tree = grid[idx_y][idx_x]
    #look ahead
    visible = True
    for forward_idx in range(idx_x + 1, GRID_MAX_X):
        if(tree <= grid[idx_y][forward_idx]):
            visible = False
            break
    if visible:
        return True
    

    #look behind
    visible = True
    for forward_idx in range(idx_x - 1, -1, -1):
        if(tree <= grid[idx_y][forward_idx]):
            visible = False
            break
    if visible:
        return True

    #look down
    visible = True
    for forward_idx in range(idx_y + 1, GRID_MAX_Y):
        if(tree <= grid[forward_idx][idx_x]):
            visible = False
            break
    if visible:
        return True

    #look up
    visible = True
    for forward_idx in range(idx_y - 1, -1, -1):
        if(tree <= grid[forward_idx][idx_x]):
            visible = False
            break
    if visible:
        return True


def calculate_scenic_score(idx_x, idx_y):
    tree = grid[idx_y][idx_x]
    #look ahead
    forward_score = 0
    for forward_idx in range(idx_x + 1, GRID_MAX_X):
        forward_score += 1
        if(tree <= grid[idx_y][forward_idx]):
            break

    #look behind
    behind_score = 0
    for forward_idx in range(idx_x - 1, -1, -1):
        behind_score += 1
        if(tree <= grid[idx_y][forward_idx]):
            break

    #look down
    down_score = 0
    for forward_idx in range(idx_y + 1, GRID_MAX_Y):
        down_score += 1
        if(tree <= grid[forward_idx][idx_x]):
            break

    #look up
    up_score = 0
    for forward_idx in range(idx_y - 1, -1, -1):
        up_score += 1
        if(tree <= grid[forward_idx][idx_x]):
            break

    return forward_score * behind_score * down_score * up_score

print("PART 1:")
print(calculate_visible_trees())
print("PART 2:")
print(best_scenic_score())