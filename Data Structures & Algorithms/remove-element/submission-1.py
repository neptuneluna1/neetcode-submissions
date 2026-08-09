class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums: return len(nums)
        k = nums.count(val)
        nums.sort(key = lambda x: (x == val, x))
        print(nums)
        return len(nums) - k


        