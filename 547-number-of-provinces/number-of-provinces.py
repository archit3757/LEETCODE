class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count=0

        def dfs(i):
            nonlocal count
            visited[i]=True
            for j in range(len(isConnected[i])):
                if visited[j]==False and isConnected[i][j]:
                    dfs(j)
        for i in range(len(isConnected)):
            if visited[i]==False:
                dfs(i)
                count+=1
        return count