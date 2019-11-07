def sol_helper(newN,negFlag):
    if newN == "":
        return newN+"5"
    for n in newN:
        compN = int(n)
        if (compN < 5 and not negFlag) or (compN > 5 and negFlag):
            return "5"+ newN
        elif(compN >= 5 and not negFlag) or (compN <= 5 and negFlag):
            return n + sol_helper(newN[1:], negFlag)

def solution(N):
    negFag = False
    if N<0:
        negFag = True
    result =  int(sol_helper(str(abs(N)), negFag))
    if negFag:
        return result * -1
    else:
        return result

if __name__ == '__main__':
    print(solution(- 8000))