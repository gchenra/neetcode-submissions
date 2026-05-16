from typing import Set, Dict, List
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force: creat a separate dict of {sum: [index_pair]}
        # iterate through nums list again to find all triplet
        # use 2 pointer to calculate sums of all pairs
        sumDict: Dict[int, List(Tuple(int))] = defaultdict(list)

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                curSum = nums[i] + nums[j]
                sumDict[curSum].append((i, j))

        triplets: Set[int] = set()
        # find triplets
        for k in range(0, len(nums)):
            targetNum = 0 - nums[k]
            if targetNum in sumDict:
                pairs = sumDict[targetNum]
                # find pairs with index != to k
                for indices in pairs:
                    ind1 = indices[0]
                    ind2 = indices[1]
                    if ind1 != k and ind2 != k:
                        # put sorted tuple inside set to get all combination instead of permutations
                        triplets.add(tuple(sorted([nums[k], nums[ind1], nums[ind2]])))
        triplets = list(triplets)
        return [list(each) for each in triplets]
        # time complexity: O(n^2)

