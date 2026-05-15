class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      c = Counter(nums)
      
      common =(dict(c.most_common(1)))
      for k , v in common.items():
        element = k
        occurence = v
      if occurence > len(nums)/2:
        return element    