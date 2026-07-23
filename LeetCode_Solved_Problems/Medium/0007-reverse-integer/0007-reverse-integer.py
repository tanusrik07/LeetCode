class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1
        if x<0:
            sign = -1
            x=-x
        rev=0
        while x>0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x//10
        if -2**31 <= rev and rev <= 2**31 - 1:
            return sign*rev
        return 0