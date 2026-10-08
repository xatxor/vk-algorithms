# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    total = 0
    min_len = len(nums) + 1

    for right, num in enumerate(nums):
        total += num
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return min_len if min_len <= len(nums) else 0
