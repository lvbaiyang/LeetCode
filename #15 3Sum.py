class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)

        nums.sort()
        result = []
        if (length < 3):
            return result
        if (length == 3):
            if (sum(nums) == 0):
                result.append(nums)
                return result
            else:
                return result


        for i in range(length - 2):
            if (i != 0 and nums[i] == nums[i - 1]):
                continue
            if(nums[i]>0):
                break
            L = i + 1
            R = length - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] > 0):
                    R -= 1

                elif (nums[i] + nums[L] + nums[R] < 0):
                    L += 1

                else:
                    result.append([nums[i], nums[L], nums[R]])
                    R -= 1
                    while (nums[R + 1] == nums[R] and L < R):
                        R -= 1
                    L += 1
                    while (nums[L - 1] == nums[L] and L < R):
                        L += 1

        return result
nums = [-1,0,1,2,-1,-4]
a = Solution()
print(a.threeSum(nums))