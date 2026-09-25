class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = []
        n = len(nums)
        result = []
        for num in nums:
            if num not in seen: 
                seen.append(num)
                amt = nums.count(num)
                if amt > n/3:
                    result.append(num)
        return result