# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        p = head
        n = head.next
        head.next = None

        while n:
            x = n.next
            n.next = p
            p = n
            n = x

        return p