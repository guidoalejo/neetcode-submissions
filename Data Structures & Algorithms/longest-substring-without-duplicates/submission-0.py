class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0            
        right = 0
        char_set = set()    # track characters of current window
        max_length = 0      # save the longest substring

        for right in range(len(s)): # iterate through the string

            while s[right] in char_set: # if a character is already on the set
                # we must shrink the window from the left
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])  # add new character to the window

            max_length = max(max_length, right - left + 1)

        return max_length

