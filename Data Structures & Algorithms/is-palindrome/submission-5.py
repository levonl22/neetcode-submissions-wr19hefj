class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for char in s:
            if char.isalnum():
                new += char
        return new == new[::-1]