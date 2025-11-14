class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Define values
        currentCount = 0
        maxCount = 0
        #Iterate arrays
        for num in nums:
            if num == 1:
                currentCount+1
            else:
                currentCount = 0
            
            if currentCount > maxCount:
                maxCount = currentCount

        return maxCount

