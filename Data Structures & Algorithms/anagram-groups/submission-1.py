from collections import defaultdict
from typing import Dict, Tuple
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force: put all words into different sets
        # create a map of word to their sets
        # iterate through word list and put words with same letter set
        # into same sublist
        # time complexity: avg word length, m. O(n + n*m)
        # space complexity: O(n*m)
        # alternative way: use the sorted word as dictionary key
        # after sorting each anagram word become the same
        # alternative, use a fixed length frequency array as dictionary key
        count_arr_to_word_map: Dict[Tuple[int]:str] = defaultdict(list)
        for s in strs:
            count_arr = [0] * 26
            for char in s:
                count_arr[ord(char) - ord('a')] += 1
            count_arr_to_word_map[tuple(count_arr)].append(s)
        return list(count_arr_to_word_map.values())