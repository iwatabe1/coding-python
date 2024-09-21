import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Creating Linked list
stack = collections.deque([5, 4, 3, 2, 1, 0])
head = ListNode(stack.pop())
pos = head  # call by reference 参照渡し
while stack:  # stack が空になるまで
    pos.next = ListNode(stack.pop())
    pos = pos.next

# get val from Linked list
while head is not None:
    print(head.val, end=" ")
    head = head.next
