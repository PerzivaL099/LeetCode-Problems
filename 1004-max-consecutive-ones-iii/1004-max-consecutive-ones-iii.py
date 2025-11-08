class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       #Pointers
        left = 0
        zeroCount = 0
        maxLen = 0
        #Iterate 
        for right in range(len(nums)):

            #Add value to window
            if nums[right] == 0:
                zeroCount += 1

            #Check if window is invalid
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            #Update maximum
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
