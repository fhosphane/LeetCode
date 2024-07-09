class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        x = 0
        liste = []
        for a in range(0,len(customers)):
            if customers[a][0] > x:
                x = customers[a][0]
            x += customers[a][1]
            liste.append(x - customers[a][0])
        return sum(liste) / len(liste)