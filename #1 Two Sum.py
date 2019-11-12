class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, num in enumerate(nums):
            if num in hashMap:
                return [index, hashMap[num]]
            else:
                hashMap[target - num] = index