class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
    
    if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
                return
            grid[r][c] = 'W'  # Mark the land as visited by converting 'L' to 'W'
            # Explore the neighbors horizontally and vertically
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':  # Found an unvisited land
                    island_count += 1
                    dfs(r, c)
        
        return island_count
                    
        return 0
