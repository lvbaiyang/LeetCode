class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)

        tmp = []
        for i in nums:
            if tmp == [] or i > tmp[-1]:
                tmp.append(i)
            elif i < tmp[-1]:
                left, right = 0, len(tmp)-1
                while(left < right):
                    mid = int((left+right)/2)
                    if tmp[mid] == i:
                        left = mid
                        break
                    elif tmp[mid] < i:
                        left = mid+1
                    elif tmp[mid] > i:
                        right = mid
                tmp[left] = i

        return len(tmp)

nums = [3,5,6,2,5,4,19,5,6,7,12]
a = Solution()
print(a.lengthOfLIS(nums))