class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        arr=[]
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
            if dic[nums[i]]>len(nums)//3 and nums[i] not in arr:
                arr.append(nums[i])
        return arr