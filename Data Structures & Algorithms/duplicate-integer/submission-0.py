class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        shashank_hash = set()

        for n in nums: 
            if(n in shashank_hash):
                return True

            shashank_hash.add(n)
        
        return False

        

        