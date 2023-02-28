class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dd = [0] * (n+1)
        if len(dd) >= 2:
            dd[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                dd[i] = dd[i //2]
            else:
                dd[i] = dd[i//2] + dd[i//2 + 1]
        return max(dd)