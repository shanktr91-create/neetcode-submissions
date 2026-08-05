class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        size = len(s1)

        left = 0
        right = size-1
        hash_set = {}
        hash_set_ref = {}
        for i in s1:
            hash_set_ref[i]= hash_set_ref.get(i, 0) + 1

        while(right<len(s2)):

            for i in range(left,right+1):
                hash_set[s2[i]]= hash_set.get(s2[i], 0) + 1

            if hash_set == hash_set_ref:
                return True
            
            else:

                hash_set = {}
                left+=1
                right+=1

        
        return False
            

        