class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        dc = {}
        dl = []
        for key,v in c.items():
            if v ==1 :
                dc[key]=v
                dl.append(key)

        
        if len(dl) < int(k) :
            return ""
        return dl[k-1]


        