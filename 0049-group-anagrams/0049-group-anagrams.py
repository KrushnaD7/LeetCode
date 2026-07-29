class Solution:
    
    # def sor(self,o):
        
    #     sorted(o)
    #     print(o)
    #     return str(o)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    #     a = {}

    #     for s in strs:
    #         key = self.sor(s)

    #         if a[key] not in a:
    #             a[key] = s
    #         else:
    #             a[key].append(s)


    #     return list[a.values()]

        groups = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())

        