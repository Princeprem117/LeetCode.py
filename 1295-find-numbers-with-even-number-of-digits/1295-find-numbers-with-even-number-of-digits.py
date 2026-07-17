class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for i,n in enumerate(nums):
            if len(str(abs(n))) %2==0:
                ans+=1
        return ans
