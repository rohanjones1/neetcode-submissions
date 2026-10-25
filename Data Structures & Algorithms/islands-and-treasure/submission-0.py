class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                newX = x+dx
                newY = y+dy

                if newX in range(0, len(grid)) and newY in range(0, len(grid[0])) and grid[newX][newY] != -1 and grid[newX][newY] > grid[x][y] + 1:
                    grid[newX][newY] = grid[x][y] + 1
                    q.append((newX, newY))




            

