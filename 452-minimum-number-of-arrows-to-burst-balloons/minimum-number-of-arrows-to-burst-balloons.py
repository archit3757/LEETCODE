class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        count=1
        def f(l):
            return l[1]
        points.sort(key=f)
        maxi=points[0][1]
        for i in range(1,len(points)):
            print(points[i])
            if maxi<points[i][0]:
                count+=1
                maxi=points[i][1]
        return count
