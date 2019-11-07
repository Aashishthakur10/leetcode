import math
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        minm = self.getMin()
        if minm is None or x < minm:
            minm = x
        self.stack.append((x, minm))


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack)>0:
            return self.stack[-1][-1]
        else:
            return None




if __name__ == '__main__':

    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    # obj.pushs(5)
    # obj.pushs(8)
    # obj.pop()
    obj.push(2)
    obj.push(0)
    obj.push(3)
    obj.push(0)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())