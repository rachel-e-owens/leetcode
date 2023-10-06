class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = num_ops = 0
        j = len(nums) - 1
        nums.sort()

        while (i < j):
            sum = nums[i] + nums[j]
            if (sum == k):
                num_ops += 1
                i += 1
                j -= 1
            elif (sum < k):
                i += 1
            else:
                j -= 1
        
        return num_ops


s = Solution()
nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
print(s.maxOperations(nums, k))