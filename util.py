def create_grid(grid):
    """create a 4x4 array of zeroes within a grid"""
    for i in range(4):
        lst = []
        for x in range(4):
            lst.append(0)
        grid.append(lst)

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(4):
        print("|", end = "")
        for x in range(4):
            if(grid[i][x]==0):
                print("     ", end = "")
            else:
                print("{0:<5}".format(grid[i][x]), end = "")
        print("|")
    print("+--------------------+")
 
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    val = False
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x]>=32:
                val = True          
    return val

def check_lost (grid):
    """return True if there are no 0 values and there are no
    adjacent values that are equal; otherwise False"""
    for i in range(4):
        for x in range(4):
            if grid[i][x] == 0:
                return False
            if(i!=3 and x!=3):
                if(grid[i][x]==grid[i][x+1] or grid[i][x]==grid[i+1][x]):
                    return False
    return True    

def copy_grid (grid):
    """return a copy of the given grid"""
    grid_new = []
    for i in grid:
        lst = []
        for x in i:
            lst.append(x)
        grid_new.append(lst)
    return grid_new

def grid_equal (grid_1, grid_2):
    """check if 2 grids are equal - return boolean value"""
    if grid_1 == grid_2:
        return True
    else:
        return False