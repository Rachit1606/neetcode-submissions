class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for i in nums:
            hm[i] = hm.get(i,0) + 1
        
        for k in hm:
            if hm.get(k) > len(nums)/2:
                return k 
        