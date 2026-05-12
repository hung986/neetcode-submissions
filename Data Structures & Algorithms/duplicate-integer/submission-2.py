class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        countMap = {}
        for num in nums:
            # If countMap does not contain name
            if num not in countMap:
                countMap[num] = 1
            else:
                countMap[num] += 1
                return True
            if len(nums) == len(set(nums)):
                return False