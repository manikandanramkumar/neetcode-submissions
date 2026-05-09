class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        dup = []
        for i in nums:
            if i not in seen:
                seen.append(i)
            else :
                dup.append(i)
        return bool(dup)

        