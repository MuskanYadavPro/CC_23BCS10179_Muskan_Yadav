class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = [0] * 35
        for n in nums:
            for i in range(35):
                if n & (1 << i):
                    count[i] += 1
        res = 0
        mod = 10 ** 9 + 7
        for j in range(k):
            cur = 0
            for i in range(35):
                if count[i]:
                    count[i] -= 1
                    cur += 1 << i
            res += cur * cur % mod
        return res % mod
