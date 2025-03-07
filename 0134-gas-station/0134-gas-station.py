class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gost = 0
        go = 0
        new = 0
        for a in range(len(gas)):
            gost += gas[a] - cost[a]
            go += gas[a] - cost[a]
            if go < 0:
                go = 0
                new = a + 1
        if gost < 0:
            return -1
        return new

