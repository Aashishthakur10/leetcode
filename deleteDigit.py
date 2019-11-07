def deleteDigit(n):
    strVal = str(n)
    index = 0
    min = 9999
    for i in range(len(strVal)):
        tst = int(strVal[i])
        if int(strVal[i]) < min:
            min = int(strVal[i])
            index = i

    return int(strVal[:index] + strVal[index+1:])

if __name__ == '__main__':
    print(deleteDigit(1001))