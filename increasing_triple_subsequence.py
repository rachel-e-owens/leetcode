import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # initialize smallest and second_smallest as max int
        # iterate through nums 
        # if nums[i] <= smallest -> smallest = nums[i]
        # elif nums[i] <= second_smallest -> second_smallest = nums[i]
        # else: this number is larger than smallest AND second smallest
        # and we have 3 increasing numbers so we can return true
        # otherwise, return false

        result = False
        small = sys.maxsize
        smaller = sys.maxsize

        for n in nums:
            if n <= smaller:
                smaller = n
            elif n <= small:
                small = n
            else:
                result = True
        
        return result
        
s = Solution()
n = [ 5, 4, 3, 2, 1 ]
print(s.increasingTriplet(n))