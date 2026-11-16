class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = defaultdict(int)

        if len(s) != len(t): return False

        for i in range(len(s)):
            anagram[s[i]] += 1
            anagram[t[i]] -= 1

        for k,v in anagram.items():
            if v!=0: return False
        return True



        