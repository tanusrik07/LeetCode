class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        num = x
        while num >0:
            rem = num % 10
            rev = rev * 10 + rem
            num = num//10
        return rev==x