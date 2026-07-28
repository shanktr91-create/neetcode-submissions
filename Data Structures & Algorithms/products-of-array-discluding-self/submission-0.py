class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod_excl = [1] * len(nums)
        prefix_prod_excl[0] = 1
        for i in range(1, len(nums)):
            prefix_prod_excl[i] = prefix_prod_excl[i-1] * nums[i-1]
        suffix_prod_excl = [1] * len(nums)
        suffix_prod_excl[-1] = 1

        for i in range(len(nums) - 2, -1, -1):
            suffix_prod_excl[i] = suffix_prod_excl[i + 1] * nums[i + 1]
        res = [0]* len(nums)
        for i in range(len(nums)):
            res[i] = prefix_prod_excl[i] * suffix_prod_excl[i]
        
        return res