class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        arr=nums[:len(nums)//2:]
        lists=nums[len(nums)//2::]
        lists=lists[::-1]
        maxi=0
        total=0

        final=[]
        for i in range(len(lists)):
            total=arr[i]+lists[i]
            maxi=max(total,maxi)

        return maxi