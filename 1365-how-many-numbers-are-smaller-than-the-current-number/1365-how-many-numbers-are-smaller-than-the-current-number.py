class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #0.-Store number of instances
        result = []
        #1.- Iterate through List
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                #2.-Compare current number with others
                if nums[j] < nums[i]:
                    #increase count when its smaller
                    count += 1
            #4.-add results to new array
            result.append(count)
        return result
        
        