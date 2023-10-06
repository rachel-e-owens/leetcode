#Given an array of characters chars, compress it using the following algorithm:

#Begin with an empty string s. For each group of consecutive repeating characters in chars:

#If the group's length is 1, append the character to s.
#Otherwise, append the character followed by the group's length.
#The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

#After you are done modifying the input array, return the new length of the array.

#You must write an algorithm that uses only constant extra space.

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = "" 
        current_char = ''
        next_char = ''
        current_length = 0

        if (len(chars) == 1):
            return 1

        for x in range(len(chars)-1):
            current_char = chars[x]
            current_length = 1
            next = x + 1
            next_char = chars[next]
            #print(current_char)
            while (next_char == current_char and next <= len(chars)):
                #print(next_char)
                current_length += 1
                next += 1
                next_char = chars[next]
            
            if current_length > 1:
                s += current_char
                chars[next-1] = current_length                
        

s = Solution()
chars = ["a","a","b","b","c","c","c"]
s.compress(chars)

# have 1 pointer and have same_char flag
# start iterating through array
# while i < len(chars)
# 