class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c1 = Counter(chars)
        res = 0

        
        for w in words:
            cur_word = defaultdict(int)
            flag = True
            for c in w :
                cur_word[c] +=1
                if cur_word[c] > c1[c]:
                    flag = False
                    break
            if flag :
                res += len(w)
        return res

