class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x = {}
        if not len(s) == len(t):
            return False
        else:
            for l in range(len(s)):
                if s[l] in x and x[s[l]] != t[l]:
                    return False
                elif s[l] not in x and t[l] in x.values():
                    return False
                elif not s[l] in x:
                    x[s[l]] = t[l]


        return True

# def isIsomorphic(self, s, t):
#         return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))
if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("paper","title"))
