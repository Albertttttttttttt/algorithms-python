def numIslands(grid):
    def dfs(p, n):
        if p < 0 or n < 0 or p >= k or n >= s or grid[p][n] == '0':
            return
        grid[p][n] = '0'
        dfs(p+1,n)
        dfs(p-1,n)
        dfs(p,n+1)
        dfs(p,n-1)

    k = len(grid)
    s = len(grid[0])
    count = 0
    for i in range(k):
        for j in range(s):

    return count