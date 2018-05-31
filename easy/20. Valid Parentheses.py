"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        left_ = "{[("
        right_ = "}])"
        save_l = []
        for item in s:
            if item in left_:
                save_l.append(item)
            if item in right_:
                if len(save_l) > 0:
                    if left_.index(save_l[-1]) == right_.index(item):
                        save_l.pop()
                    else:
                        return False
                else:
                    return False
        if len(save_l) == 0:
            return True
        return False
