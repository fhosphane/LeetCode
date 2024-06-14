class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        second = []
        last = []
        for a in points:
            second.append((a[0] ** 2) + (a[1] ** 2))
        for b in range(0,k):
            x = second.index(min(second))
            last.append(points[x])
            second[x] = (10 ** 8) * 2 + 1
        return last
        