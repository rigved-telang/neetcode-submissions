class Solution:
    def dfs(self, grid, r, c, visited):
        ROWS, COLS = len(grid), len(grid[0])
        if (min(r, c) < 0 or \
            r == ROWS or c == COLS or \
            visited[r][c] == 1 or \
            grid[r][c] == "0"):
            return
        
        visited[r][c] = 1
        self.dfs(grid, r-1, c, visited)
        self.dfs(grid, r+1, c, visited)
        self.dfs(grid, r, c-1, visited)
        self.dfs(grid, r, c+1, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_isl = 0
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0" or visited[i][j] != 0:
                    continue
                
                num_of_isl += 1
                self.dfs(grid, i, j, visited)
        
        return num_of_isl