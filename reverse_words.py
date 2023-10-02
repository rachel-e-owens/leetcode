class Solution:
    def reverseWords(self, s: str) -> str:
        # put words into an array
        # for each word, extract the characters and put into a char array
        # reverse the characters
        # put back into a string and back in the array
        # print the array as string

        #edge cases:
        # if one word
        # if one letter

        s = s.split(" ") # split sentence at each space

        for x in range(len(s)):
            s[x] = s[x][::-1]
        
        return ' '.join(s)           




s = Solution()
fullString = "Let's take a LeetCode contest"
print(s.reverseWords(fullString))