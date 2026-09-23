from collections import defaultdict
from typing import Dict, Tuple, List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input valid. all lower case? could input be emtpy, can they all fit into memory?
        # either trade off memory or trade off time, can use a 26 long tuple to represent the letter count for each string, or sort each string in place, the tuple and the sorted string will then be used as the key in the hashmap
        # correction: the sort solution doesn't save memory. 
        ana_dict: Dict[str:List[str]] =  defaultdict(list)

        for str in strs:
            sorted_str = ''.join(sorted(str))
            ana_dict[sorted_str].append(str)
        
        return list(ana_dict.values())
            
        