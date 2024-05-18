class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        liste = []
        alist = []
        alist.append(1)
        liste.append([1])
        if numRows == 1:
            return liste
        for a in range(numRows):
            if len(alist) == a+1:
                liste.append(alist)
            else:
                if len(alist) == 1:
                    alist.append(1)
                else:
                    blist=[1]
                    for b in range(len(alist)):
                        if b<len(alist)-1:
                            blist.append(alist[b]+alist[b+1])
                    blist.append(1)
                    alist = blist
                    liste.append(alist)
        return liste