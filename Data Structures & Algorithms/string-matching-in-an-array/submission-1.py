class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                print(i,j)
                if i == j:
                    # print(words[i] + " " + words[j])
                    continue
                print(words[i] + " " + words[j])
                if words[i] in words[j]:
                    res.append(words[i])
                    print(words[i] + " " + words[j])
                    # break
        return list(set(res))
