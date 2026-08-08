class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for n in nums1:
            for m in nums2:
                if n==m and n not in ans:
                    ans.append(n)
        return ans