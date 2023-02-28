from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        p = len(prices)
        q = [1] * p
        n = 1
        for i in range(1, p):
            if prices[i - 1] - prices[i] == 1:
                q[i] = q[i - 1] + 1
            n += q[i]
        return n
