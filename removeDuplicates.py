class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        c = 0
        while i < len(nums)-1:
            if nums[i] is nums[i+1]:
                del nums[i+1]
                # nums.pop(i+1)
                c+=1

            i+=1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))