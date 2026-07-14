class Solution:
    def subtractProductAndSum(self, num: int) -> int:
        p=1
        s=0
        for n in str(num):
            n=int(n)
            p*=n
            s+=n
        return p-s