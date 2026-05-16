class Solution:
    def isPalindrome(self, s: str) -> bool:
        # put two pointers at the front and end of the string
        # move them inward to the middle of the string
        # check if each value pointed are equal
        # stop when left pointer >= right pointer

        # clarification: ignore case? empty str result
        l, r = 0, len(s) - 1
        while l < r:
            # skip none alpha numeric 
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l , r = l + 1, r - 1
        return True        