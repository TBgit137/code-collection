# 找出数组中只出现过一次的数字
# ^ 异或操作

class Solution:
    def single_number(self, nums: List[int]) -> int:
        single = nums[0]

        for num in nums[1:]:
            single ^= num

        return single