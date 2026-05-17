class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        # srt = dict(sorted(c.items() ,key = lambda x : x[1] ,reverse =True ))
   
        od , ev = [],[]
        for k,v in c.items():
            
            if v%2 ==1 :
                od.append(v)
            else :
                ev.append(v)
        print(od , ev)
        print(max(od))
        print(max(ev))
        return (max(od) - min(ev))
        