from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums):
        total_distinct = len(set(nums))
        n = len(nums)
        result = 0
        left = 0
        freq = defaultdict(int)

        for right in range(n):
            freq[nums[right]] += 1

            while len(freq) == total_distinct:
                result += (n - right)
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return result

        

