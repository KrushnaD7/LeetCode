class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        p = 1
        s = 0
        while temp>0:
            l = temp%10
            temp = temp // 10
            p = p*l
            s = s+l
        return p-s    

        