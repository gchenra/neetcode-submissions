class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1: sort then compare
        # solution 2: create a count array (length 26) of frequency for each letter
        # key function is ord
        # solution 3: create hashmap of of letter frequency, directly compare the maps
        arr_s, arr_t = [0] * 26, [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(0, len(s)):
            arr_s[ord(s[i].lower()) - ord('a')] += 1
            arr_t[ord(t[i].lower()) - ord('a')] += 1
        
        return arr_s == arr_t
        