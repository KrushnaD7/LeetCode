class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p = 0
        b = prices[0]
        for i in range(1,n):
            if b>prices[i]:
                b = prices[i]

            if prices[i] - b > p:
                p = prices[i] - b

        return p 

        