class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        t_max = nums[0]
        for i in range(1,len(nums)):
            curr_max = max(nums[i]+nums[i-1],nums[i])
            nums[i]=curr_max
            t_max = max(curr_max,t_max)

        return t_max



if __name__ == '__main__':
    v = Solution()
    print(v.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))