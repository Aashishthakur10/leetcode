class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[1 for x in range(m)] for x in range(n)]
        # res[0][0] = 1
        # res[0].append(1)
        # print("kb")
        for i in range(1,n):
            for j in range(1,m):
                res[i][j]= res[i-1][j]+res[i][j-1]

        return res[-1][-1]




if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7,3))
