def lastSubstring(s: str) -> str:
    # index = {c: i for i, c in enumerate(sorted(set(s)))}
    sortedVal = sorted(set(s))
    index = {}
    value = 0
    for i in sortedVal:
        index[i]=value
        value+=1

    radix, val, cur, lo = len(index), 0, 0, 0

    for i in range(len(s) - 1, -1, -1):
        cur = index[s[i]] + cur / radix
        if cur >= val:
             lo, val = i, cur


    return s[lo:]


if __name__ == '__main__':
    print(lastSubstring("xydb"))