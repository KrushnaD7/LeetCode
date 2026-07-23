class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # a = 0
        # for i in range(low,high+1):
        #     if i%2!=0:
        #         a+=1

        # return a


        return (high+1)//2 - low//2

        