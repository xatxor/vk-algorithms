# https://leetcode.com/problems/sort-array-by-parity/

from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    even_index = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[even_index], nums[i] = nums[i], nums[even_index]
            even_index += 1

    return nums
