class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # int
        maxV = 0
        i = 0
        while i<len(prices)-1:
            if prices[i+1]-prices[i] > 0:
                maxV+= prices[i+1]-prices[i]
            i+=1
        return maxV


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,2,3,4,5]))