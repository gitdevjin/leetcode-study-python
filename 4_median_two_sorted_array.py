# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        pointerA = 0
        pointerB = 0
        result = []

        while pointerA < len(nums1) and pointerB < len(nums2):
            if nums1[pointerA] <= nums2[pointerB]:
                result.append(nums1[pointerA])
                pointerA += 1
                # print("pointerA : " + str(pointerA))
                # print("Resut after A : " + str(result))
            else:
                result.append(nums2[pointerB])
                pointerB += 1
                # print("pointerB : " + str(pointerB))
                # print("Resut after B : " + str(result))

        if pointerA == len(nums1):
            rest = nums2[pointerB:]
            result = result + rest
            
        if pointerB == len(nums2):
            rest = nums1[pointerA:]
            result = result + rest
            # print(result)
        
        if len(result) % 2 == 1:
            mid = len(result) // 2
            return result[mid]

        else:
            mid = len(result) // 2
            mid2 = (len(result) // 2) - 1
            # print("result Len : " + str(len(result)))
            # print("mid : "  + str(mid))
            # print("mid 2: " + str(mid2))
            return (result[mid] + result[mid2]) / 2

solObj = Solution()
output = solObj.findMedianSortedArrays([1,2], [3, 4])

print("output : " + str(output))