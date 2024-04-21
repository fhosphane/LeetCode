class Solution:
    def mySqrt(self, x: int) -> int:
        a = True
        num = 0
        while a:
            if x>=num ** 2 and x<(num+1) ** 2:
                return num
            num += 1