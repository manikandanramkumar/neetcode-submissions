class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        
        for i in range(0,2*n):
            if i <= n-1:
                ans.append(nums[i])
            else:
                ans.append(nums[i-n])
        
        return ans
            