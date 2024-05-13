class Solution:
    def sumBase(self, n: int, k: int) -> int:
        output = 0
        while not n//k < k:
            output += n - (n//k) * k
            n = n//k
        output += (n - (n//k) * k) + n//k
        return output
        