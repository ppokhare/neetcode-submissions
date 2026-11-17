class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        topK = defaultdict(int)

        for n in nums:
            topK[n] +=1


        sortedTopK = sorted(topK.items(), key = lambda x: x[1], reverse = True)


        return [x[0] for x in sortedTopK[:k]]

