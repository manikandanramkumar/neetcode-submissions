class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = len([ d[11:13] for d in details if int(d[11:13]) > 60])
        return count