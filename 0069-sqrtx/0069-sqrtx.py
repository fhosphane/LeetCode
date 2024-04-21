class Solution:
    def mySqrt(self, x: int) -> int:
        num = 0
        while not x<(num+1) ** 2:
            num += 1
        return num