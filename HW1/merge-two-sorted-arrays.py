# https://leetcode.com/problems/merge-sorted-array/

from typing import List


def mergeSortedArrays(arr1: List[int], arr2: List[int]) -> List[int]:
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
