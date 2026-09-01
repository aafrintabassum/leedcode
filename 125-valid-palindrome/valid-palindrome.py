class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        n=""
        for ch in s:
            if ch.isalnum():
                n+=ch
        r=n[::-1]
        if r==n:
            return True
        return False