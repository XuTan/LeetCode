"""

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = ""
        for i in s:
            if i.isalnum() or i.isalpha():
                ss += i.lower()
        for index in range(len(ss)//2):
            if ss[index] != ss[len(ss) - index - 1]:
                return False
        return True
