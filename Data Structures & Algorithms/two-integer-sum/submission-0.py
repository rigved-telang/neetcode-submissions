class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            if target - num in hm:
                return [hm.get(target-num), i]
            
            hm[num] = i
        
        return [-1, -1]