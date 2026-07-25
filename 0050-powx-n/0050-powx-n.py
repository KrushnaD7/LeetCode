class Solution:
    def pow(self, x: float, n: int):
        if n == 0:
            return 1

        a = self.pow(x,n//2)
        if n%2==0:
            return a*a  
        else:
            return a*a*x


    def myPow(self, x: float, n: int) -> float:
        # # without recursion 
        # if n>=0:
        #     return x**n
        # else:
        #     return 1/(x**(-1*n))


        if n >=0:
            return self.pow(x,n)
        else:
            return 1/self.pow(x,n*(-1))


        