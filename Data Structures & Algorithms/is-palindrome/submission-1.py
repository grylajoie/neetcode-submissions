class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ''.join(filter(str.isalnum, s))
        left = 0
        right = len(s1) - 1
        while left < right:
            if s1[left] != s1[right]:
                return False
            else:
                left = left + 1
                right = right - 1
        return True
        

                
        