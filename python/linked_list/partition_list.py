class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def partition(self, head: ListNode, x: int) -> ListNode:
        less_dummy = self.ListNode(0)
        greater_dummy = self.ListNode(0)

        less_pointer = less_dummy
        greater_pointer = greater_dummy

        current = head
        while current:
            if current.val < x:
                less_pointer.next = current
                less_pointer = less_pointer.next
            else:
                greater_pointer.next = current
                greater_pointer = greater_pointer.next
            current = current.next

        less_pointer.next = greater_dummy.next
        greater_pointer.next = None

        return less_dummy.next
