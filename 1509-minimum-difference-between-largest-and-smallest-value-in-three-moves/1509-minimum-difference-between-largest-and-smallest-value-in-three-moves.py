class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        snums = sorted(nums)
        a = len(nums) - 4
        minik = max(nums) - min(nums)
        for b in range(0,len(nums)):
            if b+a < a + 4:
                if snums[b+a] - snums[b] < minik:
                    minik = snums[b+a] - snums[b]
        return minik
