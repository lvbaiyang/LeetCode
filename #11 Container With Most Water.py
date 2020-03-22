class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol = 0
        i = 0;j = len(height)-1
        while i != j:
            if height[i] < height[j]:
                if height[i]*(j-i) > vol:
                    vol = height[i]*(j-i)
                i+=1
            else:
                if height[j]*(j-i) > vol:
                    vol = height[j]*(j-i)
                j-=1

        return vol

height = [1,8,6,2,5,4,8,3,7]
a = Solution()
print(a.maxArea(height))