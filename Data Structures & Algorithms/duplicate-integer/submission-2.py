class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_list=set(nums)
        if(len(nums)>len(set_list)):
            return True
        return False

