class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        l = len(nums2)
        for n in nums1:
            idx = nums2.index(n)
            nxt = -1
            for j in range(idx, l):
                if nums2[j] > n :
                    nxt = nums2[j]
                    break
            result.append(nxt)
        return result