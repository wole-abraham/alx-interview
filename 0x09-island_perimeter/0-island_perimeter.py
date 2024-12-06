def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a binary grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    # Validate grid dimensions
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")

    rows = len(grid)
    cols = len(grid[0])

    if not (1 <= rows <= 100 and 1 <= cols <= 100):
        raise ValueError("Grid dimensions must be between 1 and 100")

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for the cell itself
                perimeter += 4

                # Subtract 1 for each neighboring land cell
                if i > 0 and grid[i - 1][j] == 1:  # Check top neighbor
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Check left neighbor
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check bottom neighbor
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Check right neighbor
                    perimeter -= 1

    return perimeter

