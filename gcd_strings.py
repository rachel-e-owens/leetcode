class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        max_length = 0
        if str1 == str2:
            return str1
        elif str1 + str2 != str2 + str1:
            return ""
        
        list = [str1, str2]
        shortest = min(list, key=len)
        longest = max(list, key=len)

        for x in range(1,len(shortest)+1):
            s = shortest[0:x]
            if longest + s == s + longest and len(longest) % len(s) == 0 and len(shortest) % len(s) == 0:
                max_length = x
                
        return shortest[0:max_length]


s = Solution()
s.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")

# get which str is shorter
# 