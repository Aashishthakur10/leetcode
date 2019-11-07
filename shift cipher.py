import re
# def rot13(message):
#     # your code here
#     alph = {}
#     str = ""
#     wrd = ord('a')
#     wrd2 = ord('A')
#     for i in range(26):
#         alph[chr(wrd + i)] = i
#         alph[chr(wrd2 + i)] = i
#
#     for m in message:
#         if not m.isalpha():
#             str += m
#         else:
#             t = alph[m]
#             t = (t + 13) % 26
#             if m.isupper():
#                 chng = wrd2
#             else:
#                 chng = wrd
#             p = chr(t+chng)
#             str += p
#
#     return str

# def rot13(message):
#   return message.encode('rot13')

def rot13(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)


if __name__ == '__main__':
    print(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."))