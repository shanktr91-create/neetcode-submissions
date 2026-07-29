class Solution:
    def isPalindrome(self, s: str) -> bool:
        ed_str = []
        for i in s: 
            if i.isalnum(): 
                ed_str.append(i.lower())
        
        start = 0
        end = len(ed_str)-1
        res = True
        while ((start <= end)):
            if ed_str[start] == ed_str[end]:
                start+=1
                end-=1
                continue
            else:
                res = False
                break
        return res

