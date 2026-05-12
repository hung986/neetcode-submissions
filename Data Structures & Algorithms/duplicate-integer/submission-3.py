class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for num in nums:
            # If countMap does not contain name
            if num in countMap:
                return True
            countMap[num] = 1
        return False