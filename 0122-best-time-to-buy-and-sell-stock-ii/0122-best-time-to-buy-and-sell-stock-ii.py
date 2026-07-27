class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # p = 0 

        # b = prices[0]

        # for i in range(1,n):
        #     if b > prices[i]:
        #         b = prices[i]

        #     if prices[i] - b > p:
        #         p = p + (prices[i] - b)  
        #         b = prices[what to place here ]


        
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit

        if p < 0:
            return 0
        return p    