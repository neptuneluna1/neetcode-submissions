class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        count_list = []
        last_num = 1
        for num in nums:
            if num == last_num:
                count +=1
            else:
                count_list += [count]
                count = 0
        count_list += [count]
        return max(count_list)