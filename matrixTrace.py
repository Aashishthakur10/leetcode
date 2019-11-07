def matrixTrace(matrix):
    length = len(matrix)
    sum = 0
    for i in range(length):
        sum +=matrix[i][i]

    return sum


if __name__ == '__main__':
    print(matrixTrace([[1, 1, 1,1,1],
          [0, 5, 0,1,1],
          [2, 1, 3,1,1],
          [2, 1, 3,1,1]]))