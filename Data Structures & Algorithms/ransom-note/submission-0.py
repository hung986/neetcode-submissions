class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashMap = {}
        for i in magazine:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        
        for x in ransomNote: 
            if x not in hashMap or hashMap[x] == 0:
                return False
            hashMap[x] -= 1
        return True
        
        