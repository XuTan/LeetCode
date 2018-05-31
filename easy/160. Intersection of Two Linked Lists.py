"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = ListNode(0)
        A.next = headA
        B = ListNode(0)
        B.next = headB
        A_length = self.get_length(A)
        B_length = self.get_length(B)
        if A_length < B_length:
            length_sec = B_length - A_length
            for i in range(length_sec):
                B = B.next
        if A_length > B_length:
            length_sec = A_length - B_length
            for i in range(length_sec):
                A = A.next
        while A.next and B.next:
            if A.next == B.next:
                return A.next
            A = A.next
            B = B.next
        return None
