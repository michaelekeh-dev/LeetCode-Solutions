class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
 
        for i in range(n - 2):
            # Once nums[i] is positive, no triplet can sum to 0 (array is sorted).
            if nums[i] > 0:
                break
            # Skip duplicate anchors so we never build the same triplet twice.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
 
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate values on both pointers.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
 
        return result
 