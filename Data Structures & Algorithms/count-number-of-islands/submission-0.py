class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r, c):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            grid[r][c] = "0"
            for s, d in directions:
                new_r = s+r
                new_c = d+c
                if new_r in range(0, rows) and new_c in range(0, cols) and grid[new_r][new_c] == "1":
                    bfs(new_r, new_c)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        return islands


