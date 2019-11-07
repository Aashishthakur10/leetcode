def lexicalOrder(n):
    key = []
    curr = 1
    for i in range(n):
        key.append(curr)
        if n >= curr*10:
            curr=curr*10
        elif curr+1<=n and curr%10 is not 9:
            curr+=1
        else:
            while (curr // 10)%10 is 9:
                curr = curr//10
            curr = curr//10+1
    return key

if __name__ == '__main__':
    print(lexicalOrder(1111))