from collections import defaultdict
from typing import Dict, List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # all numbera valid not python limit, the size of the array won't be too large for memory, array can be empty?
        # create a dict of target - num as key, and index of num as value
        # iterate through the nums list second time, to find if a pair exists or not 
        # comp_ind_map: Dict[int, List[int]] = defaultdict(list)
        # for ind, num in enumerate(nums):  
        #     comp_ind_map[target - num].append(ind)
        
        # for ind, num in enumerate(nums):
        #     if num in comp_ind_map:
        #         return [ind, comp_ind_map[num][1]] if len(comp_ind_map[num]) > 1 else [ind, comp_ind_map[num][0]]

        # let's try do it without the dict of list, then you do a nested loop O(n^2)
        # or you can do dict with one pass
        ind_map: Dict[int, int] = defaultdict()
        for ind, num in enumerate(nums):
            comp = target - num
            if comp in ind_map:
                # important to put cur ind last
                return [ind_map[comp], ind]
            ind_map[num] = ind
        return []
