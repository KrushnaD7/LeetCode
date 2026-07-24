class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        a = 0
        while n>0:
            r = n%10
            if num % r == 0:
                a+=1
            n//=10

        return a
