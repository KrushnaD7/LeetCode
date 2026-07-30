class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)

        if a[0] == "-":
            ans = -int(a[1:][::-1])
        else:
            ans = int(a[::-1])

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans
        