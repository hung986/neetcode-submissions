class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L, R = 0, len(nums) - 1
        
        while L <= R:
            if nums[L] != val:
                L += 1
            else:
                nums[L], nums[R] = nums[R], nums[L]
                R -= 1
        return L
            