class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HM = {}
        for num in nums:
            if HM.get(num) is None:
                HM[num] = 1
            else:
                return True
        
        return False
        