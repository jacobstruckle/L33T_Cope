class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def get_k_nodes(node, k):
            """Returns the k-th node and the count of nodes traversed."""
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return node, count

        def reverse_linked_list(start, end):
            """Reverses the linked list from start to end."""
            prev = None
            curr = start
            while curr != end:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        dummy = self.ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            kth_node, count = get_k_nodes(prev_group_end.next, k)
            if count < k:
                break

            group_start = prev_group_end.next
            group_end = kth_node

            reversed_group_start = reverse_linked_list(group_start, group_end)

            prev_group_end.next = reversed_group_start
            group_start.next = group_end

            prev_group_end = group_start

        return dummy.next
