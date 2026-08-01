class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1={}
        h2={}

        for i in s:
            if i in h1:
                h1[i]+=1
            else:    
                h1[i]=1

        for i in t:
            if i in h2:
                h2[i]+=1
            else:    
                h2[i]=1

        return h1==h2        



# WELL IF THE SOLUTION IS NEEDED TO BE O(1) COMPLEXITY THEN
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)              