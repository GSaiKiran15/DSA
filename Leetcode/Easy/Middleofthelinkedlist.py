# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        # Best method

        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow

        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length == 1:
            return head
        mid = length // 2
        index = 0
        while head:
            head = head.next
            index += 1
            if index == mid:
                return head
