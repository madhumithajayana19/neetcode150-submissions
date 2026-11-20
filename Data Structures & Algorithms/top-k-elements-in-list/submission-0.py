class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for num in nums:
            hm[num]=hm.get(num,0)+1
        sorted_keys = sorted(hm, key=hm.get, reverse=True)
        return sorted_keys[0:2]
        