class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        m = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        l = []

        for i in range(k):
            l.append(m[i][0])

        return l