class Solution:
    def isPalindrome(self, x):
        if str(x)[::-1] == str(x):
            return True