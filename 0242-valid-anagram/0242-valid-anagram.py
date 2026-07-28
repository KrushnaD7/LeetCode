class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return str(list(s).sort()) == str(list(t).sort()) just trying to solve in one line but ...

        a = {}
        b = {}

        if len(s) != len(t):
            return False  

        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = 1
            if s[i] in a:
                a[s[i]] += 1

            if t[i] not in b:
                b[t[i]] = 1
            if t[i] in b:
                b[t[i]] += 1

        print(a,b)
        return a == b



        