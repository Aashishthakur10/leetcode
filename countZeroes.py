
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    for i in range(length):
        if nums[i] is 0:
            nums.remove(0)
            nums.append(0)

    return nums


if __name__ == '__main__':
    print(moveZeroes([0,1,0,3,12]))

            