class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        count=0
        for i in range(len(costs)):
            if coins<costs[i]:
                break
            count+=1
            coins-=costs[i]
        return count

