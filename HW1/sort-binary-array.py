# https://leetcode.com/problems/sort-colors/

from typing import List


def sortBinaryArray(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] == 0:
            left += 1
        elif nums[right] == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums
