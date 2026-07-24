class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)

        a = []

        for i in candies:
            if i+extraCandies>=max_c:
                a.append(True)
            else:
                a.append(False)
        return a        
        