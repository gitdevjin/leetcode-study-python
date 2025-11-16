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


######################## ChatGPT Answer #############################
### Read and Absorb
class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s

        start, end = 0, 0  # indices of longest palindrome found

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return the length of palindrome
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length palindrome
            l1, r1 = expand(i, i)
            # Even length palindrome
            l2, r2 = expand(i, i + 1)

            # Choose the longer one
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]