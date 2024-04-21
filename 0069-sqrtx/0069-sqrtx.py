class Solution:
    def mySqrt(self, x: int) -> int:
        num = 0
        while x>=(num+1) ** 2:
            num += 1
        return num