class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = i = 0
        j = len(height) - 1

        while (i < j):
            cur_min = min(height[i], height[j])
            new_height = cur_min * (j - i)
            if (new_height > max):
                max = new_height
            
            if cur_min == height[i]:
                i += 1
            else:
                j -= 1

        return max


s = Solution
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
s.maxArea(heights)