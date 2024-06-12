class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        a = nums.count(1)
        b = nums.count(2)
        while a != 0:
            nums.remove(1)
            nums.append(1)
            a -= 1
        while b != 0:
            nums.remove(2)
            nums.append(2)
            b -= 1
            