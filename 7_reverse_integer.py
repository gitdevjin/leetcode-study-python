# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

# Constraints:

# -231 <= x <= 231 - 1

class Solution(object):
    def reverse(self, x):
        limit = self.overflowLimit(2,31)
        mark = 1
        if x < 0 :
            x = x * -1
            mark = -1

        str_arr = str(x)
        int_arr = []
        reversed = str_arr[::-1]

        for s in reversed:
            int_arr.append(int(s))

        output = 0
        for n in int_arr:
            output = output * 10 + n

        if mark < 0:
            output = output * -1

        if output >= limit:
            return 0
        elif output < -1 * limit:
            return 0

        return output 
    
        """
        :type x: int
        :rtype: int
        """
    
    def overflowLimit(self, num, times):
        result = 1
        if times == 0:
            return result
        
        for i in range(times):
            result = result * num
        
        return result
    
sol = Solution()
answer = sol.overflowLimit(2, 31)
output = sol.reverse(-1234)
print(output)

######## ######## ######## ######## ######## ######## ######## ######## #########
######### ######## ######## ######## GPT Answer ####### ####### ######## ########
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check overflow before multiplying
            if reversed_num > (INT_MAX - digit) // 10:
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num 

