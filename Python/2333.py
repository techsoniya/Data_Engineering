# 2333. Minimum Sum of Squared Difference
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

# The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

# You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

# Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

# Note: You are allowed to modify the array elements to become negative integers.

 

# Example 1:

# Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
# Output: 579
# Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
# The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.
# Example 2:

# Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
# Output: 43
# Explanation: One way to obtain the minimum sum of square difference is: 
# - Increase nums1[0] once.
# - Increase nums2[2] once.
# The minimum of the sum of square difference will be: 
# (2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
# Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.
 

# Constraints:

# n == nums1.length == nums2.length
# 1 <= n <= 105
# 0 <= nums1[i], nums2[i] <= 105
# 0 <= k1, k2 <= 109




class Solution:
    def minSumSquareDiff(
        self,
        nums1: list[int],
        nums2: list[int],
        k1: int,
        k2: int
    ) -> int:

        # 1. Calculate differences
        diff = []
        for i in range(len(nums1)):
            diff.append(abs(nums1[i] - nums2[i]))

        operations = k1 + k2

        # 2. If all differences can become zero
        if sum(diff) <= operations:
            return 0

        # 3. Find the smallest achievable maximum difference
        left = 0
        right = max(diff)

        while left < right:
            target = (left + right) // 2

            needed = 0
            for d in diff:
                if d > target:
                    needed += d - target

            if needed <= operations:
                right = target
            else:
                left = target + 1

        target = left

        # 4. Reduce differences greater than target
        needed = 0
        for d in diff:
            if d > target:
                needed += d - target

        remaining = operations - needed

        # 5. Calculate squared sum after reducing to target
        total = 0
        for d in diff:
            total += min(d, target) ** 2

        # 6. Use leftover operations to reduce target to target - 1
        count = sum(1 for d in diff if d >= target)
        reduce_count = min(remaining, count)

        total -= reduce_count * (2 * target - 1)

        return total
