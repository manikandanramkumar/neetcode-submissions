class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []
        for user in emails:

                idx = user.split("@")[0].find("+")
                domain = user.split("@")[1]
                filtered =user[0:idx].replace(".","")+"@"+domain
                result.append(filtered)
        return len(set(result))


        