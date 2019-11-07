# def same_structure_as(original,other):
#     # your code here
#     # your code here
#     if not isinstance(original, list) or not isinstance(other, list):
#         return False
#     b = ''.join(str(e) for e in original if not str(e).isspace() and not isinstance(e, str))
#     c = ''.join(str(e) for e in other if not str(e).isspace() and not isinstance(e, str))
#     if len(c) is not len(b):
#         return False
#     compare = []
#     for i in b:
#         if not i.isnumeric():
#             compare.append(i)
#         else:
#             compare.append("y")
#     for val in range(len(c)):
#         value = c[val]
#         comparis = compare[val]
#         if c[val].isnumeric() and not compare[val] is "y":
#             return False
#         elif not c[val].isnumeric() and compare[val] is not c[val]:
#             return False
#
#     return True

def same_structure_as2(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            val = same_structure_as(o1, o2)
            if not val: return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)

def same_structure_as(original, other):
    if type(original) == list == type(other):
        return len(original) == len(other) and all(map(same_structure_as, original, other))
    else:
        return type(original) != list != type(other)

if __name__ == '__main__':
    print(same_structure_as([[1,1,],1],[2,[2,2]]))
    # print(same_structure_as([1,'[',']'], ['[',']',1]))
