class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=(int("".join(map(str, digits))))
        ans=ans+1
        ans=list(map(int,str(ans)))
        return ans







        # c=0
        # for i in digits:
        #     #b=digits.index(i)#for power value
        #     a=i*pow(10,len(digits)-digits.index(i)-1)#100+20+3
        #     c=c+a
        # #d=c+1
        # return (list(map(int,str(c+1))))

