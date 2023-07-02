class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n != 0:
            return pow(x, n)
        elif n < 0:
            n = abs(n)
            return 1 / pow(x, n)
        else:
            return 1
        

'''class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n!=0:
            return pow(x,n)
        elif n<0:
            n=abs(n)
            return 1/pow(x,n)'''