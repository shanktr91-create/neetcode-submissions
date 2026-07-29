class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        fin = {}
        alpha = {}
        fin_list = []
        for i in range(97,123):
            alpha[chr(i)]=0
        
        for j in strs:

            for k in j: 
                alpha[k]+=1
            key = tuple(sorted(alpha.items()))
            if key not in fin:
                fin[key] = []

            fin[key].append(j)
            #fin[tuple(sorted(alpha.items()))].append(j)
            for i in range(97,123):
                alpha[chr(i)]=0

        for x in fin.values():
            fin_list.append(x)

        return fin_list   

        