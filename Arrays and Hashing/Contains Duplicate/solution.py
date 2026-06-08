class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in range(nums):
            if i in hashset:
                return True
            hashset.add(i)
            return False
        

nums = [1,5,2,5,3,1]

Solution(nums)
