class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0

        def bfs(curr_x, curr_y):
            grid[curr_x][curr_y] = "0"
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for x, y in directions:
                if x + curr_x in range(0, len(grid)) and y + curr_y in range(0, len(grid[0])) and grid[x+curr_x][y+curr_y] == "1":
                    bfs(x+curr_x, y+curr_y)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    bfs(i, j)
        
        return islands
        
