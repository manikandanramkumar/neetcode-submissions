class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j = 0 , 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                i +=1
            j +=1
        print(i)
        if i < len(t):
            
            return len(t) - i
        else :
            return 0
        
        