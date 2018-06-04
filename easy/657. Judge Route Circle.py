"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up, left = 0, 0
        for i in moves:
            if i == "U":
                up += 1
            elif i == "D":
                up -= 1
            elif i == "L":
                left += 1
            elif i == "R":
                left -= 1
        if up==0 and left ==0:
            return True
        else:
            return False
