class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        poss = 0
        minV=0
        minV2=0
        for i in range(0,len(height)-1):
            for j in range(i-1,-1,-1):
                minV = max(minV,height[j])
            for k in range(i+1,len(height)-1):
                minV2 = max(minV2,height[k])
            poss+= min(minV,minV2)-height[i]

        return poss

if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))