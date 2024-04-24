def islandPerimeter(grid):
    visited = set()
    row, col = len(grid), len(grid[0])
    result = []

    def dfs(x, y):
        visited.add((x, y))
        stack = [(x, y)]
        min_row, min_col = x, y
        max_row, max_col = x, y
        while stack:
            cur_x, cur_y = stack.pop()
            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = cur_x + dx, cur_y + dy
                if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited and grid[ny][nx] == 1:
                    stack.append((nx, ny))
                    visited.add((nx, ny))
                    min_row = min(min_row,nx)
                    min_col = min(min_col,ny)
                    max_row = max(max_row,nx)
                    max_col = max(max_col,ny)
        return min_row, min_col, max_row, max_col
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1 and (i, j) not in visited:
                min_row, min_col, max_row, max_col = dfs(i,j)
                result.append([min_row, min_col, max_row, max_col])

    return result




grid1 = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
print(islandPerimeter(grid1))
