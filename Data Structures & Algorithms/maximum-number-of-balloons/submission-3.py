class Solution:
    
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        lt1= [c['b'],c['a'],c['n']]
        lt2 = [c['l'],c['o']]
       
        print(min(lt1))
        print(min(lt2))
        print(min(lt2)//2)
        if  min(lt1) >= min(lt2)//2  :
            return min (lt2)//2
        else :
            return 0
        # if (c['a'] == c['b'] == c['n'] )& (c['l']==c['o'] ==2*(c['a'])):
        #     return c['a']
        # else :
        #     return 0
        