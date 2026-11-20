class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}
        for i in s:
            if hm1.get(i) is None:
                hm1[i] = 1
            else:
                hm1[i] = hm1.get(i) + 1
        
        for i in t:
            if hm2.get(i) is None:
                hm2[i] = 1
            else:
                hm2[i] = hm2.get(i) + 1

        return hm1 == hm2
         



        