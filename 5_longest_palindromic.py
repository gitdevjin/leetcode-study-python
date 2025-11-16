# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution(object):
    def longestPalindrome(self, s):
        output = []
        record = []
        length = 0
        for i in range(len(s) - 1):
            for j in (range(len(s), i, -1)):
                mid = (j - i) // 2 + i
                #abbbba mid = 3
                if (j - i) % 2 == 1: # len is odd
                    left = s[i:mid]
                    right = s[mid+1:j][::-1]
                    print("mid : " + str(mid) + " i : " + str(i) + ", j : " + str(j) + ", left: " + str(left) + ", right: " + str(right))
                    if left == right:
                        output = s[i:j]
                        if len(output) > length:
                            record = output[:]
                            length = len(output)
                    print(str(record))        
                        
                else: # len is even
                     left = s[i:mid]
                     right = s[mid:j][::-1]
                     print(", mid : " + str(mid) + " i : " + str(i) + ", j : " + str(j) + ", left: " + str(left) + ", right: " + str(right))
                     if left == right:
                         output = s[i:j]  
                         if len(output) > length:
                             record = output[:]
                             length = len(output)
                     print(str(record))
        return record
    

sol = Solution()
answer = sol.longestPalindrome("abbc")
print("answer: " + answer)