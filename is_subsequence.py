class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = ""
        i = j = 0
        while (i < len(t) and j < len(s)):
            if (t[i] == s[j]):
                x += t[i]
                i += 1
                j += 1
            else:
                i += 1
        
        if s == x:
            return True
        
        return False


sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s,t))