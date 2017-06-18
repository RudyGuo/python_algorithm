# https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description

# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_dup_index =0
        res = 0
        char_index = dict()
        for i in range(0,len(s)):
            if s[i] in char_index:
                max_dup_index = max(char_index[s[i]]+1,max_dup_index)
            res = max(res, i - max_dup_index+1)
            char_index[s[i]] = i
        return res


print Solution().lengthOfLongestSubstring("abba")
