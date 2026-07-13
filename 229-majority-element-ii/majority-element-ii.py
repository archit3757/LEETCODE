class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ele1='null'
        count1=0
        count2=0
        ele2='null'
        for i in range(len(nums)):
            if nums[i]==ele1:
                count1+=1
            elif nums[i]==ele2:
                count2+=1
            elif count1!=0 and count2!=0:
                count1-=1
                count2-=1
            elif count1==0:
                count1+=1
                ele1=nums[i]
            elif count2==0:
                count2+=1
                ele2=nums[i]
        if nums.count(ele1)>len(nums)/3 and nums.count(ele2)>len(nums)/3:
            return[ele1,ele2]
        
        elif nums.count(ele2)>len(nums)/3:
            return[ele2]
        
        elif nums.count(ele1)>len(nums)/3:
            return[ele1]
        else:
            return []
        
