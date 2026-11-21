import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x>=0 and x<10:
            return True
        A = [int(i) for i in str(x)]
        size = len(A)
        middle = math.ceil(size / 2)
        for i in range(middle):
            if A[i] != A[-i - 1]:
                return False
        return True
