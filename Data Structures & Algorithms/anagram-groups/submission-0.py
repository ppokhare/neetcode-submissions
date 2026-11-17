class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        gAnagram = defaultdict(list)


        for str in strs:
            list_str = [0]*26
            for char in str:
                list_str[ord(char)- 97] +=1

            gAnagram[tuple(list_str)].append(str)

            # gAnagram[Counter(str)].append(str) counter is unhashable, use a tuple of size 26, even list is unhashable



        
        return list(gAnagram.values())