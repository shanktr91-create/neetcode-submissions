class Solution:
    def largestRectangleArea(self, heights:List[int])->int:
        arr = heights[:]         
        max_area = 0
        level = 1

        while any(h > 0 for h in arr):

            width = 0

            for i in range(len(arr)):

                if arr[i] > 0:
                    width += 1
                    arr[i] -= 1
                else:
                    max_area = max(max_area, width * level)
                    width = 0

            # Handle a segment that reaches the end
            max_area = max(max_area, width * level)

            level += 1

        return max_area


