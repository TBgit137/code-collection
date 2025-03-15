# 链表中是否有环
# 快慢指针
# 相遇后，慢指针再走一圈，相遇时，走的长度就是环的长度

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> int:
        if not head:
            return False

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                length = 1
                current = slow.next
                while current != slow:
                    current = current.next
                    length += 1
                return length

        return False