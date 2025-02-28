class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for innum in range(len(nums)):
            answer = [innum]
            first = nums[innum]
            nums[innum] = 'a'
            if target-first in nums:
                answer.append(nums.index(target-first))
                return answer
        return False


            