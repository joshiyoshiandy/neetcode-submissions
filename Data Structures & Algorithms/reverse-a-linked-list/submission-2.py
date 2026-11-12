# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        p = None
        cur = head
        n = head.next
        
        while cur:
            cur.next = p
            p = cur
            cur = n

            if n:
                n = n.next

        return p
        