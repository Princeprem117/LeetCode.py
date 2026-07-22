class Solution:
    def addDigits(self, num: int) -> int:
        ans=0
        while num >9:
            num=sum(int(n) for n in str(num) )
        return num