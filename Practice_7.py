
import math
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if (A == 0):
            return 0
        else:
            A = math.sqrt(A)
            if (A % (math.floor(A)) != 0):
                return int(math.floor(A))
            else:
                return int(math.floor(A))
sol=Solution()
print(sol.sqrt(49))
print(sol.sqrt(64))
print(sol.sqrt(59))


_____________________________________________________


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        Flag=True
        for row in A:
            if(B not in row):
                Flag = False
            else:
                return 1
        if (Flag== False):
            return 0


_______________________________________________________



