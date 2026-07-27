class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace(".","[.]")    lol



        # a=  address.split(".")
        # b = "[.]".join(a)


        
        b = ""
        for i in address:
            if i == ".":
                b = b + "[.]"
            else:
                b = b + i

       
        


        return b

    


        