class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        ss = s.split()
        return len(ss[-1])