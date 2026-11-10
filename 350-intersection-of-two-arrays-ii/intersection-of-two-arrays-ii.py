class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l=[]
        dic={}
        for i in nums1:
            if i in nums2:
                if i not in dic:
                    dic[i]=min(nums1.count(i),nums2.count(i))
        for i in dic:
            l.extend([i]*dic[i])
        return l    






                

        