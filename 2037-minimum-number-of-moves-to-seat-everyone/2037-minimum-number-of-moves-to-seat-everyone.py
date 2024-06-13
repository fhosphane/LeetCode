class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        b = 0
        for a in range(0,len(seats)):
            b += abs(sorted(seats)[a] - sorted(students)[a])
        return b
    