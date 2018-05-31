"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        l = ListNode(0)
        p = l
        plus_flag = 0
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + plus_flag) % 10)
            plus_flag = (l1.val + l2.val + plus_flag) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val + plus_flag) % 10)
                plus_flag = (l1.val + plus_flag) // 10
                l1 = l1.next
                p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val + plus_flag) % 10)
                plus_flag = (l2.val + plus_flag) // 10
                l2 = l2.next
                p = p.next
        if plus_flag == 1:
            p.next = ListNode(1)
        return l.next
