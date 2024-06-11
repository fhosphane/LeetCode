class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        liste = []
        for a in range(0,len(arr2)):
            b = arr1.count(arr2[a])
            while b != 0:
                liste.append(arr2[a])
                arr1.remove(arr2[a])
                b -= 1
        return liste + sorted(arr1)
            
            
                