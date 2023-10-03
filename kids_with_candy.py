class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        kids_with_greatest_num_candies = []
        max_candies = 0
        for x in candies:
            if (x > max_candies):
                max_candies = x
        
        for y in candies:
            if (y + extraCandies >= max_candies):
                kids_with_greatest_num_candies.append(True)
            else:
                kids_with_greatest_num_candies.append(False)
        
        return kids_with_greatest_num_candies

s = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
kids_with_greatest_num_candies = s.kidsWithCandies(candies, extraCandies)
print(kids_with_greatest_num_candies)


# get the max among the candies array
# go through candies array and add extraCandies to each one
# if it is >= max then that that is true