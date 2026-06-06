from collections import deque
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # DFS with backtracking, backtrack when curSum > target
        # question how to keep track of uniqueness? Record all results as set, 
        # so it deduplicate automatically
        results = set()

        def DFS(curSum:int, curCombo: List[int]) -> None: 
            if curSum > target:
                return
            elif curSum == target:
                sortedCombo = tuple(sorted(curCombo))
                results.add(sortedCombo)
                return
            # TODO: maybe other base case

            for num in nums:
                DFS(curSum+num, curCombo + [num])
        
        # for each num do DFS on them
        DFS(0, [])
        
        return [list(t) for t in results]