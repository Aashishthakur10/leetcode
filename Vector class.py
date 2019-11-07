from math import sqrt
import operator as op
# import map

# import math
# # class Vector:
# #     # TODO: Finish the Vector class.
# #     def __init__(self, data = []):
# #         self.data = data
# #
# #     def add(self, ob2):
# #         newObj = Vector()
# #         if len(ob2.data) == len(self.data):
# #             for i in range(len(ob2.data)):
# #                 newObj.data.append(operate(self.data[i], ob2.data[i], 1))
# #             return newObj
# #         else:
# #             raise Exception("length String mismatch")
# #
# #     def subtract(self, ob2):
# #         newObj = Vector()
# #         if len(ob2.data) == len(self.data):
# #             for i in range(len(ob2.data)):
# #                 val = operate(self.data[i], ob2.data[i], 2)
# #                 newObj.data.append(val)
# #             return newObj
# #         else:
# #             raise Exception("length String mismatch")
# #
# #     def dot(self, ob2):
# #         sum = 0
# #         if len(ob2.data) == len(self.data):
# #             for i in range(len(ob2.data)):
# #                 sum += operate(self.data[i], ob2.data[i], 3)
# #             return sum
# #         else:
# #             raise Exception("length String mismatch")
# #
# #     def norm(self):
# #         sum = 0
# #         for i in range(len(self.data)):
# #             sum += self.data[i] ** 2
# #         return math.sqrt(sum)
# #
# #     def __str__(self):
# #         if len(self.data) > 0:
# #             res = "(" + str(self.data[0])
# #
# #             for i in range(1, len(self.data)):
# #                 res += "," + str(self.data[i])
# #             return res + ")"
# #         else:
# #             raise Exception("Empty String")
# #
# #     def equals(self, ob2):
# #         if len(ob2.data) == len(self.data):
# #             for i in range(len(self.data)):
# #                 if ob2.data[i] != self.data[i]:
# #                     return False
# #             return True
# #         else:
# #             return False
# #
# #
# # def operate(a, b, ops):
# #     if ops is 1:
# #         return a + b
# #     elif ops is 2:
# #         return a - b
# #     elif ops is 3:
# #         return a * b
# #
# #
# # if __name__ == '__main__':
# #     a = Vector([1, 2, 3])
# #     b = Vector([3, 4, 5])
# #     a.add(b).equals(Vector([4, 6, 8]))
# #     print(a.subtract(b).equals(Vector([-2, -2, -2])))
# #     # print(a.subtract(b))
# #     # print("asd")




class Vector:
    # TODO: Finish the Vector class.
    def __init__(self, array=[]):
        self.__data = array

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        return iter(self.__data)

    def __getitem__(self, i):
        return self.__data[i]

    def check_length(f):
        def wrapper(self, other):
            if len(self) != len(other):
                raise ValueError()
            return f(self, other)

        return wrapper

    @check_length
    def add(self, other):
        res = Vector(map(op.add, self, other))
        return res

    @check_length
    def subtract(self, other):
        res = Vector(map(op.sub, self, other))
        return res

    @check_length
    def dot(self, other):
        res = reduce(op.add, map(op.mul, self, other))
        return res

    def norm(self):
        return sqrt(self.dot(self))

    def equals(self, other):
        if len(self) != len(other):
            return False
        return all(map(op.eq, self, other))

    def __str__(self):
        return '(%s)' % ','.join(str(x) for x in self.__data)


if __name__ == '__main__':
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])
    a.add(b).equals(Vector([4, 6, 8]))
    print(a.subtract(b).equals(Vector([-2, -2, -2])))
    # print(a.subtract(b))
    # print("asd")