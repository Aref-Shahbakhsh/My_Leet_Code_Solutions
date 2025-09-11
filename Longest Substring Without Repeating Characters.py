class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        max_word = ''
        max_length_list = [-1]

        if s == '':
            return 0

        for i in range(len(s)):
            for j in s:
                if j not in max_word:
                    max_length += 1
                    max_word = max_word + j
                else:
                    max_length_list.append(max_length)
                    max_length = 0
                    max_word = ''
                    s = s[1:]
                    break
        if max_length > max(max_length_list):
            return max_length
        return max(max_length_list)

        
