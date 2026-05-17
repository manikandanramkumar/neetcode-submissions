class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        
   
        od , ev = [],[]
        for k,v in c.items():
            
            if v%2 ==1 :
                od.append(v)
            else :
                ev.append(v)
   
        return (max(od) - min(ev))
        