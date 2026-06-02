class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for k,v in c.items():
            if not v%2 == 0:
                return False
        return True
        
        