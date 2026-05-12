class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        strs = sorted(strs,key=len)
        # print(strs)
        for i in range(len(strs[0])):
            # print(output)
            for s in strs:
                # print(s)
                if s[i] !=strs[0][i] :
                    print("here")
                    # print(strs[0][i])
                    return output
        
            output += strs[0][i]
        return output
            