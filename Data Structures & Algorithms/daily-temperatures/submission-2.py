class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        temp_stack = []
        temp_val = [0] * n

        for i in range(n - 1, -1, -1):

            while temp_stack and temperatures[i]>=temperatures[temp_stack[-1]]:
                temp_stack.pop()

            if temp_stack:
                temp_val[i] = temp_stack[-1]-i

            else:
                temp_val[i] = 0
            temp_stack.append(i)

        return temp_val
            
