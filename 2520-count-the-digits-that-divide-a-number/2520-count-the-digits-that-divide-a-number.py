class Solution:
    def countDigits(self, num: int) -> int:
        ans=0
        temp=num

        while temp>0:
            n=temp%10

            if num%n==0:
                ans+=1
            temp//=10
        return ans