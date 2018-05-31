"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_len = len(strs)
        if strs_len == 0:
            return ""
        if strs_len == 1:
            return strs[0]
        com_str = strs[0]
        for s in strs[1:]:
            j = 0
            min_len = min(len(s), len(com_str))
            while j < min_len:
                if com_str[j] != s[j]:
                    break
                j += 1
            if j == 0:
                return ""
            com_str = com_str[:j]
        return com_str
