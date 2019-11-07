import re


def top_3_words(text):
    """
    re.finditer(pattern, string, flags=0)
    Return an iterator yielding match objects over all non-overlapping matches
    for the RE pattern in string. The string is scanned left-to-right, and matches are returned
    in the order found. Empty matches are included in the result.
    :param text:
    :return:
    """
    wordList = []
    wordDiff = []
    i = 0
    max = 1
    while i < len(text)-1:
        val = ord(text[i])
        while val is 39 or (64 < val < 123):
            i += 1
            val = ord(text[i])
        else:
            if len(wordList) > 0:
                curr = i - wordList[-1]
                if curr > max:
                    max = curr
                wordDiff.append((curr, wordList[-1], i))
            wordList.append(i)

            i += 1

    wordDiff.sort(key = takeFirst)

    for i in range(len(wordDiff)):
        if wordDiff[i][0] == 1:
            continue
        else:
            words = wordDiff[i]
    print(max)

def takeFirst(elem):
    return elem[0]




if __name__ == '__main__':
    print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))
