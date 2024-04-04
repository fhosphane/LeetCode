class Solution:
    def maxLength(self, arr: List[str]) -> int:
        from itertools import chain, combinations
        def all_subsets(lst):
            return chain(*map(lambda x: combinations(lst, x), range(0, len(lst)+1)))
        
        
        subsets = list(all_subsets(arr))
        maxi = 0
        for i in range(len(subsets)):
            if len(set("".join(subsets[i]))) == len("".join(subsets[i])):
                if maxi < len("".join(subsets[i])):
                    maxi = len("".join(subsets[i]))
        return maxi
        
            
