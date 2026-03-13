class Solution(object):

    def partition(self,nums, mid):
        ops = 0
        for x in nums:
            ops += (x + mid - 1) // mid
        return ops


    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        l = len(nums)
        left = 1
        right = max(nums)

        while left<right:
            mid = (left+right)//2
            if self.partition(nums,mid) <= l+maxOperations:
                right = mid
            else:
                left = mid + 1

        return left























