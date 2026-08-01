class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # a = []
        # for i in nums:
        #     b=0
        #     for j in nums:
        #         if i>j:
        #             b+=1
        #     a.append(b)
        # return a

        
        d = {}
        s = sorted(nums)

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i

        ans = []
        for num in nums:
            ans.append(d[num])

        return ans