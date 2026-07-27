class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        # b = ""
        # for i in a[::-1]:
        #     b = b + " " +i
        # return b 

        return (" ").join(a[::-1])


        