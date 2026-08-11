class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            rest = set(nums[i+1:])
            remainder = target - nums[i]
            if remainder in rest:
                ans.append(i)
                ans.append(nums[i+1:].index(remainder) + i+1)
                return ans
        return ans
            