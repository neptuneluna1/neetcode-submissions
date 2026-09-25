class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums = sorted(nums)
        counter = []
        count = 1
        lastNum = nums[0]
        for num in nums[1:]:
            if num == lastNum + 1:
                count += 1
            elif num == lastNum:
                continue
            else:
                counter.append(count)
                count = 1
            lastNum = num
        counter.append(count)
        return max(counter)
