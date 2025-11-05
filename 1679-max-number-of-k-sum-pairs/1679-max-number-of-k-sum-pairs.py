class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        #Initialize pointers and Operations
        left = 0
        right = len(nums) - 1
        totalOperations = 0

        #Compare numSum to k
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == k:
                # Perfect match: count the operation and eliminate the pair
                totalOperations += 1
                left += 1
                right -= 1
            
            elif current_sum < k:
                
                left += 1
                
            else: 
                right -= 1
                
        return totalOperations
        