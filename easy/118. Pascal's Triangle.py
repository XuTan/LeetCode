"""

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        tem = [0, 1]
        l = []
        for i in range(numRows):
            sub_l = []
            for j in range(len(tem) - 1):
                sub_l.append(tem[j] + tem[j + 1])
            l.append(sub_l)
            tem = sub_l[:]
            tem.insert(0, 0)
            tem.append(0)
        return l
