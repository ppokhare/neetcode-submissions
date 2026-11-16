class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in twoSum:
                return [twoSum[nums[i]], i]
            twoSum[target- nums[i]] = i


        