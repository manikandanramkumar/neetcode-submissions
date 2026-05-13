class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range (numRows-1):
            prev = [0] + res[-1] + [0]
            curr =[]
            for j in range(len(prev) -1) :
                curr.append(prev[j] + prev[j+1])
            res.append(curr)
        return res
        
        