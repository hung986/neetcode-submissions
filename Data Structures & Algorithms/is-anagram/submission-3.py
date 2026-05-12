class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c not in hashMap:
                hashMap[c] = 1
            else:
                hashMap[c] += 1
        
        for i in t:
            if i not in hashMap or hashMap[i] == 0:
                return False
            hashMap[i] -= 1
        return True