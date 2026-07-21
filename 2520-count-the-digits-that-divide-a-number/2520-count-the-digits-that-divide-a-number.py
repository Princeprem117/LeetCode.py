class Solution:
    def countDigits(self, num: int) -> int:
        ans=0
        for n in str(num):
            n=int(n)
            if num%n==0:
                ans+=1
        return ans