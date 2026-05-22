class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i,n in enumerate(s):
                if n in t:
                    t = t.replace(n, '', 1)
                else:
                    return False
            return True
        else:
            return False    