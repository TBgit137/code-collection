# 找到链表交点
# 遍历一个链表将其结点存储在集合中，在另一个链表中寻找相同结点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set = set()
        temp = headA

        while temp:
            node_set.add(temp)
            temp = temp.next

        temp = headB
        while temp:
            if temp in node_set:
                return temp
            temp = temp.next
        return None
