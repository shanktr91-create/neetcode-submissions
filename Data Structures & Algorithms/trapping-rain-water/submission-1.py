class Solution:
    def trap(self, height: List[int]) -> int:
        maxim = max(height)
        cols = len(height)

        # Create the map
        mapo = [[0] * cols for _ in range(maxim)]

        for col in range(cols):
            h = height[col]
            for row in range(maxim - 1, maxim - h - 1, -1):
                mapo[row][col] = 1

        volume = 0

        # Scan each row
        for i in range(maxim):

            start = False
            water = 0

            for j in range(cols):

                if mapo[i][j] == 1:
                    if start:
                        volume += water
                    start = True
                    water = 0

                elif start:
                    water += 1

        return volume



                



