# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev

if __name__ == '__main__':
    obj1 = ListNode(5)
    obj1.next = ListNode(8)
    obj1.next.next = ListNode(7)
    t = Solution()
    v = t.reverseList(obj1)
    print(v)
