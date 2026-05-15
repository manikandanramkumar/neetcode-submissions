class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sd = defaultdict(list)
            td = defaultdict(list)
            for i in range(len(s)):
                sd[s[i]].append(i)
                td[t[i]].append(i)
            s_result = {}
            t_result = {}
            i,j =0,0
            for (k,v) in (sd.items()):
                s_result[i] = v
                i +=1
            for k,v in td.items():
                t_result[j] =v
                j +=1

            if s_result == t_result:
                return True
            else :
                return False