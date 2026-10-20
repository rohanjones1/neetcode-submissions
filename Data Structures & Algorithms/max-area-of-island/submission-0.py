class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def dfs(x, y):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            total = 0
            grid[x][y] = 0
            for dx, dy in directions:
                curr_x, curr_y = dx+x, dy+y
                if (curr_x) in range(0, len(grid)) and (curr_y) in range(0, len(grid[0])) and grid[curr_x][curr_y] == 1:
                    total += dfs(curr_x, curr_y)
            return 1 + total

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
