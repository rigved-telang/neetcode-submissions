class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        def bfs(i, j):
            neighbours = [[1,0], [-1,0], [0,1], [0, -1]]
            ROWS, COLS = len(grid), len(grid[0])
            visit = set()
            queue = deque()
            visit.add((i, j))
            queue.append((i, j))
            area = 0
            grid[i][j] = 0

            while queue:
                r,c = queue.popleft()
                area += 1
                for dr, dc in neighbours:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or grid[r+dr][c+dc] == 0):
                        continue
                    queue.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))
            
            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = bfs(i,j)
                    max_area = max(max_area, area)
                
        return max_area