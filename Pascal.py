
# def generate(numRows):
#     l1 = []
#     for i in range(numRows):
#         l2 = [1]
#         for j in range(i):
#             length = len(l1[i-1])
#             if j != length-1:
#                 l2.append(l1[i-1][j]+l1[i-1][j+1])
#             else:
#                 l2.append(1)
#
#         l1.append(l2)
#
#     return l1


def generate(numRows: int):
    res=[]
    for i in range(0,numRows):
        res.append([])
        cur=0
        for j in res[i-1]:
            res[-1].append(j+cur)
            cur=j
        res[-1].append(1)
    return res

if __name__ == '__main__':

    print(generate(5))
