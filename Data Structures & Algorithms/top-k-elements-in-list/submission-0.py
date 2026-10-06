from collections import defaultdict 
from typing import Dict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # clarification question: can we assume the input is always sorted? 
        # any time complexity requirement? aim for O(n) time and space
        # first instinct: create map1 of number and frequency, them create a new map of frequency and number
        # stuck at once get the highest frequency how to get the second highest frequency number? intuitively we should use a heap. but if we want time to be O(n), then we can't use heap. 
        # map of key: number, value: frequency
        num_frq_map: Dict[int, int] = defaultdict(int) 
        for num in nums:
            num_frq_map[num] += 1
        
        # minheap to sort the frequency
        heap = []
        for num in num_frq_map.keys():
            # the first element in tuple gets sorted
            heapq.heappush(heap, (num_frq_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
