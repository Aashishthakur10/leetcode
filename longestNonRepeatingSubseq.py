class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slow = 0
        fast = 0
        maxV = 0
        setV = {}
        while fast < len(s):
            if not s[fast] in setV:
                setV[s[fast]]=fast
                fast+=1
                maxV = max(len(setV),maxV)
            else:
                del setV[s[slow]]
                slow+=1

        return maxV


if __name__ == '__main__':
    o = Solution()
    print(o.lengthOfLongestSubstring("abcabcbb"))

