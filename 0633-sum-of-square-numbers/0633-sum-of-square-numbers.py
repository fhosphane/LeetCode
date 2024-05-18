class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = int(c ** 0.5) 
        for b in range(a+1):
            if (c - (b ** 2)) ** 0.5 == int((c - (b ** 2)) ** 0.5):
                return True
        return False
            