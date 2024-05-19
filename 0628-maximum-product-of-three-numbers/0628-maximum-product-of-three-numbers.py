class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        b = []
        b.append(a[0] * a[1] * a[2])
        b.append(a[0] * a[1] * a[-1])
        b.append(a[-1] * a[-2] * a[-3])
        return max(b)