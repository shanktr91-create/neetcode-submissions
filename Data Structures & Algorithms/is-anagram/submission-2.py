class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sha_hash = dict()
        sha1_hash = dict()
        if len(s) == len(t):

            for i in s: 
                if (i in sha_hash) == True:
                    sha_hash[i]+=1
                else:
                    sha_hash[i] = 1
            for j in t:
                if (j in sha1_hash) == True:
                    sha1_hash[j]+=1
                else:    
                    sha1_hash[j] = 1

            if sha_hash == sha1_hash:
                return True

            else:
                return False
        return False
                
        
        