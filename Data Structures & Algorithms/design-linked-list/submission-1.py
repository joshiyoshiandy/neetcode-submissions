class ListNode:
    def __init__(self, v: int = -1, p = None, n = None):
        self.val = v
        self.prev = p
        self.next = n

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        res = -1
        curr = self.head.next
        
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and curr != self.tail and index == 0:
            res = curr.val

        return res

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        nx = self.head.next
        pv = self.head

        pv.next = node
        nx.prev = node
        node.next = nx
        node.pv = pv

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        nx = self.tail
        pv = self.tail.prev

        pv.next = node
        nx.prev = node
        node.next = nx
        node.prev = pv

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            node = ListNode(val)
            nx = curr
            pv = curr.prev
            pv.next = node
            nx.prev = node
            node.next = nx
            node.prev = pv

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.tail and index == 0:
            nx = curr.next
            pv = curr.prev
            nx.prev = pv
            pv.next = nx
