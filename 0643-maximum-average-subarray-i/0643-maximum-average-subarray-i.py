class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        #Initialize values
        currentWindow = sum(nums[:k])
        max_sum = currentWindow

        #Iterate
        for i in range(k, len(nums)):
            #Move the window
            currentWindow = currentWindow - nums[i - k] + nums[i]    
            #Increase max sum
            max_sum = max(max_sum, currentWindow)



        return max_sum/k


        