class Solution(object):

    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left = 0
        right = len(s) - 1

        #function to swap vowels
        def swap(x, y):
            temp = s[x]
            s[x] = s[y]
            s[y] = temp
        
        # function to check if a letter is a vowel
        def vowel(c):
            vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            return c in vowels  
          
        while(left < right):
            if (vowel(s[left]) and vowel(s[right])):
                swap(left, right)
            elif (vowel(s[left])):
                while (left < right and not vowel(s[right])):
                    right -= 1
                swap(left, right)
            elif (vowel(s[right])):
                while (left < right and not vowel(s[left])):
                    left += 1
                swap(left,right)
            left += 1
            right -= 1
        
        s = ''.join(s)
        return s

        
s = Solution()
str = "hello"
print(s.reverseVowels(str))


# swap vowels in string
# iterate using a pointer at either end
# if i or j is in [a, e, i, o, u, A, E, I, O, U]
# - increment the other until also a vowel
# - swap