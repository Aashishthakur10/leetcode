class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushs = []
        self.pops = []


    def push(self, x):
        """
        Push element x to the back of pushs.
        :type x: int
        :rtype: None
        """
        self.pushs.append(x)

    def pop(self):
        """
        Removes the element from in front of pushs and returns that element.
        :rtype: int
        """
        self.move()
        val = self.pops[-1]
        self.pops.pop(-1)
        return val


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        return self.pops[-1]



    def empty(self):
        """
        Returns whether the pushs is empty.
        :rtype: bool
        """
        return (not self.pops) and (not self.pushs)

    def move(self):

        if len(self.pops)==0:
            if len(self.pushs) is not 0:
                for i in range(len(self.pushs)-1,-1,-1):
                    self.pops.append(self.pushs.pop())




if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    queue = MyQueue()
    queue.push(1)
    print(queue.pop())
    print(queue.empty())