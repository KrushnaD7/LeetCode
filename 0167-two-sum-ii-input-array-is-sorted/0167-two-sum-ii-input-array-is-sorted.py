class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = {}

        for i in range(len(numbers)):
            if (target - numbers[i]) in a:
                return [a[target - numbers[i]]+1, i+1]

            a[numbers[i]] = i
        