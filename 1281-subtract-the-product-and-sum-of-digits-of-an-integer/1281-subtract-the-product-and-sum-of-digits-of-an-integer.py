class Solution:
    def subtractProductAndSum(self, num: int) -> int:
        p=1
        s=0
        for i,n in enumerate(str(num)):
            n=int(n)
            p*=n
            s+=n
            res=p-s
        return res