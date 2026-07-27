class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) #map alphabet count of each string to list of anagrams 
        #default implies that combo of count doesnt exist
        for s in strs: 

            count = [0]*26
            for c in s: 
                count[ord(c) - ord("a")] += 1 #ord gives ascii value

            res[tuple(count)].append(s)

        return list(res.values())