import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = math.prod(nums)
        i = 0
        for num in nums:
            if num == 0:
                nums.pop(i)
                output.append(math.prod(nums))
                nums.insert(i, 0)
            else:
                output.append(product // num)
            i += 1
        return output