class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        strs = sorted(strs,key=len)
        
        for i in range(len(strs[0])):            
            for s in strs:                
                if  s[i] !=strs[0][i] :
                    print("here")
                    
                    return output
        
            output += strs[0][i]
        return output
            