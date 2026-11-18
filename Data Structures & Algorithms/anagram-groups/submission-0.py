class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for _str in strs:
            sorted_str=tuple(sorted(_str))
            if sorted_str in hm.keys():
                hm[sorted_str].append(_str)
            else:
                hm[sorted_str]=[_str]

        return list(hm.values())
        