class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        f_sum=0
        for i in range(k):
            f_sum+=nums[i]
        max_sum= f_sum

        for i in range(k,len(nums)):
            f_sum +=nums[i]- nums[i-k]
            max_sum =max(max_sum,f_sum)
        
        return max_sum/k