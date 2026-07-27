class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele = {}

        for i in nums: 
            if (i in ele) == False:
                ele[i] = 1
            else:
                ele[i] +=1


        sorted_dict = dict(sorted(ele.items(), key=lambda x: x[1], reverse=True))
        
        items = list(sorted_dict.keys())
        ret_list = []
        count = 0
        for i in items:

            if (count>=k):
                return ret_list
            ret_list.append(i)
            count = count + 1

        return ret_list