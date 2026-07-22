class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range (len(s)):
            current = ""
            for j in range (i,len(s)):
                max_str=s[j]
                if max_str not in current:
                    current += max_str
                else:
                    break
            if len(current) > max_len:
                max_len = len(current)
        return max_len