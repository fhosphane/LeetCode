class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for a in arr:
            if a != 0:
                if a * 2 in arr or a/2 in arr:
                    return True
            else:
                if arr.count(a) > 1:
                    return True
        return False