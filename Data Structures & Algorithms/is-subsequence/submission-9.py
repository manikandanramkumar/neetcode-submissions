class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        f = True
        if  s:
            
            if (all(c in t for c in s)):
                
                tl = list(t)

                print("Target " + t)
                print("Source " + s)

                for i in range(len(s)-2):
                    print("starting source ")
                    print(tl)
                    cur = s[i]
                    nxt = s[i+1]
                    right_idx = tl.index(s[i])+1
                    print("current " + cur)
                    print("next "+ nxt)
                    print("Right range " )
                    print(tl[right_idx:len(tl)])
                    
                    if nxt in tl[right_idx:len(tl)]:
                        print("after trim")
                        del tl[0:tl.index(s[i])+1]
                        
                    else :
                        f = False
                        break
                if f :
                    left_idx = tl.index(s[-2])
                    if s[-1] in tl[left_idx:len(tl)]:
                       pass
                    else :
                        f = False
                        
            else:
                f = False
                
        
            
        return f
            

                