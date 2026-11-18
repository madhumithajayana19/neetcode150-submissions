class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for _str in strs:
            freq=[0]*26
            for ch in _str:
                freq[ord(ch)-ord('a')]+=1
            freq_tuple=tuple(freq)
            if freq_tuple in hm.keys():
                hm[freq_tuple].append(_str)
            else:
                hm[freq_tuple]=[_str]

        return list(hm.values())
        