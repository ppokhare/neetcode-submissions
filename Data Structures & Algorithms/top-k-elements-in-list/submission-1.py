class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        # n log n time
        # topK = defaultdict(int)

        # for n in nums: 
        #     topK[n] +=1

        # sortedTopK = sorted(topK.items(), key = lambda x: x[1], reverse = True)
        # return [x[0] for x in sortedTopK[:k]]

        # use heap time: k log n

        #buket sort for n 
        
        topK = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]
        
        for n in nums: 
            topK[n] +=1

        for num, count in topK.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: 
                    return res