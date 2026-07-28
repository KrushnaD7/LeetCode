class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t) just trying to solve in one line but ...

        # a = {}
        # b = {}

        # if len(s) != len(t):
        #     return False  

        # for i in range(len(s)):
        #     if s[i] not in a:
        #         a[s[i]] = 1
        #     else:
        #         a[s[i]] += 1

        #     if t[i] not in b:
        #         b[t[i]] = 1
        #     else:
        #         b[t[i]] += 1

        
        # return a == b


        c = {}


        if len(s) != len(t):
            return False  

        for i in range(len(s)):
            if s[i] not in c:
                c[s[i]] = 1
            else:
                c[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in c:
                return False
            else:
                c[t[i]] -= 1

            
            if c[t[i]] < 0:
                return False

        return True

           

        
        



        



        