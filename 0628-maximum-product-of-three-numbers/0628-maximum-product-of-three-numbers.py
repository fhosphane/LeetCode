class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        c = (a[0] * a[1] * a[2])
        if c < (a[0] * a[1] * a[-1]):
            c = (a[0] * a[1] * a[-1])
        if c < (a[-1] * a[-2] * a[-3]):
            c = (a[-1] * a[-2] * a[-3])
            
        return c