class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count_d = {}
        l = []
        for i in range(len(s)):
            if s[i] not in count_d:
                count_d[s[i]] = 1
            else :
                count_d[s[i]] +=1
        for k,v in count_d.items():
            if v < 2 :
                l.append(k)
            else:
                pass
        if not l :
            return -1
        else :
            return s.index(l[0])