class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ally = []
        for x in matrix:
            if 0 in x:
                for y in range(len(x)):
                    if x[y] == 0:
                        ally.append(y)
                    x[y] = 0
        for x in matrix:
            for y in ally:
                x[y] = 0
        