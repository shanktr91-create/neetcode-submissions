class Solution:
    def trap(self, height: List[int]) -> int:

        maxL= [0]*len(height)
        maxR = [0]*len(height)

        maxnum = 0

        for i in range(len(height)): 
            maxL[i] = max(maxnum,height[i])
            if(height[i]>maxnum):
                maxnum = height[i]
        
        maxnum = 0

        for i in range(len(height)-1,-1,-1):
            maxR[i] = max(maxnum,height[i])
            if(height[i]>maxnum):
                maxnum = height[i]
        
        volume = 0
        for i in range(len(height)): 

            volume += min(maxL[i],maxR[i]) - height[i]



        return volume



                



