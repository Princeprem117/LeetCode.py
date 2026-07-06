class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i ,l in enumerate(nums):
            if l >= target:
                return i
        return len(nums)