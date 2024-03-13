class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = range(n+1)
        for x in range(len(r)):
            if sum(r[0:x+1]) == sum(r[x:n+1]):
                return x
        return -1
