class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0,len(s)):
            if i == 0 and s[i] not in s[i+1:len(s)]:
                return i
            if i > 0 and s[i] not in s[0:i] and s[i] not in s[i+1:len(s)]:
                return i
        return -1
        