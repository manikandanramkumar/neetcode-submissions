class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def count_dict ( s:str)->dict:
            d = {}
            for i in range(len(s)):
                
                if s[i] not in d  :
                    d[s[i]] = 1
                    
                else :
                    d[s[i]] +=1
            return d    
        
        if (count_dict(s)==count_dict(t)):
            return True
        else :
            return False

        