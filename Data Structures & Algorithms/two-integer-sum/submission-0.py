from collections import defaultdict
from typing import Dict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: target - num, value: index of num
        to_target_map: Dict[int, int] = defaultdict()
        for ind, num in enumerate(nums):
            if num in to_target_map:
                return [to_target_map[num], ind]
            to_target_map[target-num] = ind
        return [-1, -1]