class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        import bisect
        frist = bisect_left(nums,target)
        last = bisect_right(nums,target)-1
        if frist<=last and frist<len(nums) and nums[frist]==target:
            return [frist , last]
        return [-1,-1]
