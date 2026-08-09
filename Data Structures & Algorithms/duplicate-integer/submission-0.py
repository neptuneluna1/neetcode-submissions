class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_nums = Counter(nums)
        for k,v in freq_nums.items():
            if v > 1: return True
        return False