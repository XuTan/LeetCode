"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        tem = [0, 1]
        while rowIndex >= 0:
            rowIndex -= 1
            tmp = []
            for i in range(len(tem) - 1):
                tmp.append(tem[i] + tem[i + 1])
            tem = tmp[:]
            tem.insert(0, 0)
            tem.append(0)
        return tem[1:-1]
