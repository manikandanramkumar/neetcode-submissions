class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        input = []
        output = []
      
        for i in range(len(grid)):
            for j in range (len(grid[i])):
                input.append(grid[i][j])
        
        c = Counter(input)
        for k,v in c.items():
            if c[k] == 2 :
                output.append(k)
        miss = set(range(1,len(input)+1))
        
        for num in set(input):
            miss.discard(num)
        output.extend(miss)
        
        return output


        