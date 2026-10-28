class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums=[]
        dic={}
        final=""
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        for key,value in dic.items():
            nums.append([key,value])
        def f(s):
            return s[1]
        nums.sort(key=f,reverse=True)

        for k in range(len(nums)):
            final+=nums[k][0]*nums[k][1]
        return(final)
