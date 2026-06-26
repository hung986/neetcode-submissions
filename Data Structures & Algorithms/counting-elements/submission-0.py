class Solution:
    def countElements(self, arr: List[int]) -> int:
        countMap = {}
        total = 0
        for a in arr:
            if a not in countMap:
                countMap[a] = 1
            else:
                countMap[a] += 1
        
        for i in range(len(arr)):
            if arr[i] + 1 in countMap:
                total += 1
            else:
                pass
        return total