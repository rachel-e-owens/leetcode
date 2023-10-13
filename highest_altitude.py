class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        alt = 0
        max_alt = alt

        for x in gain:
            alt += x
            max_alt = max(max_alt, alt)


        return max_alt
        

s = Solution()
gain = [-5,1,5,0,-7]
print(s.largestAltitude(gain))