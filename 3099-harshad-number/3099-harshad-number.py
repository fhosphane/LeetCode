class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        y = sum(map(int, list(str(x))))
        if x % y == 0:
            return y
        return -1