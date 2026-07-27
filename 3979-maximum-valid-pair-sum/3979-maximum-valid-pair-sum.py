class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        ans=0
        m_left=0
        for i in range(k,len(nums)):
            m_left = max(m_left,nums[i-k])
            ans=max(ans,nums[i]+ m_left)
        return ans