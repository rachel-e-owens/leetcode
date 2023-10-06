class Solution(object):
    def moveZeroes(self, nums):
        current = 0
        """
        for n in range(len(nums)):
            current = nums[n]
            if nums[n] == 0:
                nums.pop(n)
                nums.append(current)
        """
        i = j = 0
        while i < len(nums) and j < len(nums):
            current = nums[i]
            if nums[i] == 0 and j < len(nums):
                nums.pop(i)
                nums.append(current)
                j += 1
            else:
                i += 1

s = Solution()
nums = [0,0,1]
print(nums)
s.moveZeroes(nums)
print(nums)