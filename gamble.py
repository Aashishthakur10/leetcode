# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, K):
    # write your code in Python 3.6
    count = 0
    if K == 0:
        return N - 1
    while N > 2:

        if N % 2 == 0 and K > 0:
            N = N / 2
            K-=1
        else:
            N = N - 1
        count += 1

    return count+1


if __name__ == '__main__':
    print(solution(8,0))
