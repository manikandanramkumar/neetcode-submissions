class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        lc = []
        for i in range(len(nums)):
            if nums[i] == 1 :
                c +=1
                if i == len(nums)-1:
                    lc.append(c)
            else :
                
                lc.append(c)
                c = 0
        return max(lc)

        