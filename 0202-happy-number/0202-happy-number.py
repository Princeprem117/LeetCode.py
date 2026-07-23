class Solution:
    def isHappy(self, n: int) -> bool:
        s= set()
        while n!=0 and n not in s:
            s.add(n)
            t=0
            
            while n >0:
                d=n%10
                t+=d*d
                n//=10
            n=t
        return n==1