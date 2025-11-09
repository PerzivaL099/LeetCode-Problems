class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        #Total sum of all values
        totalSum = sum(nums)
        #Inicialize sumLeft 
        sumLeft = 0
        #Iterate through array
        for i in range(len(nums)):
            #Calcultate right side sum of values
            sumRight = totalSum - sumLeft - nums[i]

            if sumLeft == sumRight: 
                return i

            sumLeft += nums[i]
        #No partition is found
        return -1