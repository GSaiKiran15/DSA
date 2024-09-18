class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Best
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        # My solution for best algo but code is not written efficiently 
        rabbit = head
        hare = head
        while rabbit:
            if rabbit.next is not None:
                rabbit = rabbit.next.next
                hare = hare.next
                if rabbit == hare:
                    return True
            else:
                return False
            
        # not O(1) but works
        
        # lst = []
        # iterator = head
        # while iterator:
        #     if iterator in lst:
        #         return True
        #     else:
        #         lst.append(iterator)
        #     iterator = iterator.next
        # return False