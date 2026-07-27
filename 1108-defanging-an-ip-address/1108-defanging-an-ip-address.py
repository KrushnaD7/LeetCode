class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace(".","[.]")    lol


        # a = address.split()
        # b = ""
        # for i in a:
        #     if i == ".":
        #         b = b + "[.]"
        #     else:
        #         b = b + i

        a=  address.split(".")
        b = "[.]".join(a)
        


        return b

    


        