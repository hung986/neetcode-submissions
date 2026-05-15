class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(c.lower() for c in s if c.isalnum())
        L, R = 0, len(ss) - 1
        while L < R:
            if ss[L] != ss[R]:
                return False
            L += 1
            R -= 1
        return True