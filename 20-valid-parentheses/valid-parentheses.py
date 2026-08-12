class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        nums=[]
        if len(s)<2:
            return False
        for i in range(len(s)):
            if len(nums)>0 and s[i]== ')':
                if nums[-1]== '(':
                    nums.pop()
                else:
                    return False
            elif len(nums)>0 and s[i]== '}':
                if nums[-1]=='{':
                    nums.pop()
                else:
                    return False
            elif len(nums)>0 and s[i]== ']':
                if nums[-1]=='[':
                    nums.pop()
                else:
                    return False
            else:
                nums.append(s[i])
        if len(nums)==0:
            return True
        else:
            return False
            
        