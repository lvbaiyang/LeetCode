class Solution(object):

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        elif len(s) == 2:
            return 1 + int(not (s[0] == s[1]))

        flag = -1
        dict = {}
        ans = 0

        for i, c in enumerate(s):
            if c in dict.keys() and dict[c] > flag:
                flag = dict[c]
                dict[c] = i
            else:
                dict[c] = i
                ans = max(ans, i - flag)
        return ans

s = "abcabcbb"
a = Solution()
print(a.lengthOfLongestSubstring(s))