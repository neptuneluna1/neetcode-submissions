class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        amts = {}
        n = len(nums)
        for i in range(len(nums)):
            curr = nums[i]
            if curr in amts:
                amts[curr] += 1
            else:
                amts[curr] = 1
            if amts[curr] > (n / 2):
                return curr
        return max(amts)