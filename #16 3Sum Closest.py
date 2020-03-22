class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 2:
            return None
        elif len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)
        ans = float("inf")

        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > target:
                if abs(nums[i] + nums[i + 1] + nums[i + 2] - target) < abs(ans - target):
                    ans = nums[i] + nums[i + 1] + nums[i + 2]
                continue
            elif nums[i] + nums[i + 1] + nums[i + 2] == target:
                return target
            elif nums[i] + nums[-1] + nums[-2] < target:
                if abs(nums[i] + nums[-1] + nums[-2] - target) < abs(ans - target):
                    ans = nums[i] + nums[-1] + nums[-2]
                continue
            elif nums[i] + nums[-1] + nums[-2] == target:
                return target
            start = i + 1
            end = len(nums) - 1
            while (start < end):
                current = nums[i] + nums[start] + nums[end] - target

                if abs(current) < abs(ans - target):
                    ans = current + target
                elif current == 0:
                    return target
                if current < 0:
                    start += 1
                    while (nums[start] == nums[start - 1] and start < len(nums) - 1):
                        start += 1
                elif current > 0:
                    end -= 1
                    while (nums[end] == nums[end + 1] and end > 0):
                        end -= 1
        return ans

nums = [-1, 2, 1, -4]
target = 1
a = Solution()
print(a.threeSumClosest(nums, target))
