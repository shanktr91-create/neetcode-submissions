class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        items = {}
        for i in nums:
            items[i]= items.get(i,0)
        maxim = 0
        for i in nums:

        # Skip numbers that are not the start
            if i - 1 in items:
                continue

            longest = 1

            while i + 1 in items:
                longest += 1
                i += 1

            maxim = max(maxim, longest)

        return maxim 