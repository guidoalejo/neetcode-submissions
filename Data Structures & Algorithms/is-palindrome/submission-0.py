class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""

        for character in s:
            if character.isalnum():
                cleaned_string += character.lower()

        return cleaned_string == cleaned_string[::-1]