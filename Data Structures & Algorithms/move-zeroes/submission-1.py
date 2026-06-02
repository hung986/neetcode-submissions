class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return nums
        
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums
        