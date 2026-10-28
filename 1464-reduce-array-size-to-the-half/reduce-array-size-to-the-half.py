class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter
        c=Counter(arr).most_common()

        final=0
        count=0

        for i in c:
            if final>=len(arr)//2:
                return count
                break
            final+=i[1]
            count+=1
            
        return count