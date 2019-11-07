# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A,B,C)->str:
    # write your code in Python 3.6
    maxVal = max(A,B,C)
    res = " "
    dict_val = {}

    dict_val["a"] = A
    dict_val["b"] = B
    dict_val["c"] = C
    maxRange = A+B+C
    i=1
    while i<maxRange:
        if dict_val["a"] == maxVal:
            if 0<A or 0 < B or 0 < C:
                # inda+=2
                if not res[-1]=="a":
                    if maxVal == 1:
                        A-=1
                        res += "a"
                    else:
                        A-=2
                        res+="aa"
                    dict_val["a"]=A

                    if B>=C and B > 0:
                        res+="b"
                        # indb+=1
                        B-=1
                        dict_val["b"] = B
                    else:
                        if C > 0:
                            res += "c"
                            C-=1
                            dict_val["c"] = C

        if dict_val["b"]==maxVal:
            if 0<A or 0 < B or 0 < C:
                if not res[-1] == "b":
                    if maxVal == 1:
                        B-=1
                        res += "b"
                    else:
                        B-=2
                        res += "bb"
                    dict_val["b"] = B
                    if A>=C and A > 0:
                        res+="a"
                        A-=1
                        dict_val["a"] = A
                    else:
                        if C > 0:
                            res += "c"
                            C-=1
                            dict_val["c"] = C

        if dict_val["c"]==maxVal:
            if 0 < A or 0 < B or 0 < C:
                if not res[-1] == "c":
                    if maxVal == 1:
                        C-=1
                        res+="c"
                    else:
                        C -= 2
                        res += "cc"
                    dict_val["c"] = C
                    if A >= B and A > 0:
                        res += "a"
                        A -= 1
                        dict_val["a"] = A
                    else:
                        if B > 0:
                            res += "b"
                            B -= 1
                            dict_val["b"] = B



        i+=1
        maxVal = max(A,B,C)

    return res.strip()




if __name__ == '__main__':
    print(solution(6,1,1))

