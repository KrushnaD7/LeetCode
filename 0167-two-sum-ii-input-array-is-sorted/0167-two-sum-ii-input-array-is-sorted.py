class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # a = {}

        # for i in range(len(numbers)):
        #     if (target - numbers[i]) in a:
        #         return [a[target - numbers[i]]+1, i+1]

        #     a[numbers[i]] = i  this work but we go for more optimal 


        # let solve with two pointer methon here list is order so we consider 2 pointer left and right and move them according 

        l = 0
        r = len(numbers) - 1

        while l <r:

            t = numbers[l] + numbers[r]

            if t == target:
                return [l+1, r+1]
            elif t < target:
                l+=1
            else:
                r-=1
        