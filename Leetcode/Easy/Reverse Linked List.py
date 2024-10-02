class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        # values_list = []
        # node = head
        # while node:
        #     values_list.append(node.val)
        #     node = node.next
        # node = head
        # index = -1
        # while node:
        #     node.val = values_list[index]
        #     index -= 1
        #     node = node.next
        # return head
