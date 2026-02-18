# Important: All functions here are called from an external Python file.

# We import the random module (very important)
import random

# This function generates a grid.
# It does NOT display the grid, it only creates and returns it.
# The function takes three parameters:
# - height: number of rows
# - width: number of columns
# - percentageOfMine: probability of placing a mine in each cell
# Important: percentageOfMine must be a value between 0 and 1.
def gen_the_grid(height, width, percentageOfMine):
    
    # First, we create an empty list that will contain the entire grid
    grid = []

    # We loop 'height' times to create each row
    # 'i' is commonly used as a loop variable
    for i in range(height):
        
        # For each row, we create an empty list
        row = []

        # We loop 'width' times to create each cell in the row
        # 'j' is commonly used as a loop variable inside another loop
        for j in range(width):
            
            # We generate a random number between 0 and 1.
            # If the number is lower than percentageOfMine,
            # we place a mine (represented here by 11).
            if random.random() < percentageOfMine:
                
                # Add the value 11 (mine) to the row
                row.append(11)
            
            # Otherwise, we do not place a mine (represented here by 10)
            else:

                # Add the value 10 (empty cell) to the row
                row.append(10)
        
        # When the inner loop is finished, the row is complete.
        # We add this row to the grid.
        grid.append(row)
    
    # Finally, we return the generated grid
    return grid



def getNum(grid, i, j):

    # If the cell value is already less than 10,
    # it means the cell has already been revealed.
    # In that case, we simply return the grid.
    if grid[i][j] < 10:
        return grid

    # We set the current cell to 0.
    # This will be used to count the number of mines around it.
    grid[i][j] = 0

    # We check all neighboring cells around (i, j).
    # The loops go from -1 to 1 (included).
    for x in range(-1,2):
        for y in range(-1,2):

            # We skip the current cell itself.
            if x == 0 and y == 0:
                continue
            
            # Prevent errors caused by negative indices.
            # A negative index would access the opposite side of the grid in Python.
            if i + x < 0 or j + y < 0:
                continue

            try:
                # If a neighboring cell contains a mine (11)
                # or a flagged mine (13),
                # we increase the counter.
                if grid[i + x][j + y] == 11 or grid[i + x][j + y] == 13:
                    grid[i][j] += 1
            except:
                # If we go outside the grid boundaries,
                # we ignore the error.
                pass

    # If the cell is not equal to 0,
    # it means there are mines around it.
    # So we stop here.
    if grid[i][j] != 0:
        return grid

    # If the cell is still 0,
    # we recursively reveal all neighboring cells.
    for x in range(-1,2):
        for y in range(-1,2):

            # Skip the current cell
            if x == 0 and y == 0:
                continue

            # Prevent errors caused by negative indices.
            # A negative index would access the opposite side of the grid in Python.
            if i + x < 0 or j + y < 0:
                continue

            try:
                grid = getNum(grid, i + x, j + y)
            except:
                pass

    return grid


def mine(grid, i, j):

    # If the cell is already flagged (13 or 12),
    # we return "Flag".
    if grid[i][j] == 13 or grid[i][j] == 12:
        return "Flag"

    # Check if this is the very first move of the game
    isNew = True
    for a in grid:
        for b in a:
            # If any cell is already revealed (value < 10), it's not the first move
            if b < 10:
                isNew = False
                break
        if not isNew:
            break

    # If it is the first move, make sure the clicked cell and its neighbors are safe
    if isNew:
        for x in range(-1,2):  # loop over rows around the clicked cell
            for y in range(-1,2):  # loop over columns around the clicked cell
                # Set all neighboring cells (and the clicked cell) to empty (10)
                grid[i + x][j + y] = 10

    # If the cell contains a mine (11),
    # we return "Mine".
    if grid[i][j] == 11:
        return "Mine"

    # Otherwise, we reveal the cell
    # by calling getNum().
    return getNum(grid, i, j)



def flagIt(grid, i, j):

    # If the cell is already revealed (value < 10),
    # we cannot place a flag, so we return the grid as is.
    if grid[i][j] < 10:
        return grid

    # If the cell is not yet flagged (value < 12),
    # we place a flag by adding 2 to the value.
    if grid[i][j] < 12:
        grid[i][j] += 2
        return grid

    # If the cell is already flagged (value >= 12),
    # we remove the flag by subtracting 2.
    grid[i][j] -= 2
    return grid