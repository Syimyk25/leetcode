class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        chek = {}

        for i in range(len(nums)):
            if target - nums[i] in chek:
                return [i, chek[target - nums[i]]]
            else:
                chek[nums[i]] = i