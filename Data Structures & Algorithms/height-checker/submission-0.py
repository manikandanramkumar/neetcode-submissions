class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expect = sorted(heights)
        print(expect)
        c = 0
        for i in range(len(expect)):
            if expect[i] != heights[i]:
                c +=1
        return c
        