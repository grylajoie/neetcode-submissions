from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        top_k = count.most_common(k) # [(num, freq)]
        result = []
        for elem in top_k:
            num, freq = elem # each elem is (num, freq)
            result.append(num)

        return result