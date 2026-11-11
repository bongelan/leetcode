class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        m=sorted(heights)
        c=0
        for i in range(len(heights)):
            if heights[i]!=m[i]:
                c+=1
        return c

        