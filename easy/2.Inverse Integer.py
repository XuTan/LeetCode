"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
 overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg_flag = False
        if x < 0:
            neg_flag = True
            x = -x
        reverse_x = list(str(x))[::-1]
        str_x = int("".join(i for i in reverse_x))
        if neg_flag:
            str_x = -str_x
        if - 2 ** 31 <= str_x <= 2 ** 31 - 1:
            return str_x
        else:
            return 0
