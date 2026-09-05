class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if nums == []:
            return 0

        #Create dictionary
        num_dict = {}
        #Iterate through elemetnts
        for i, num in enumerate(nums):
            #calculate complement
            complement = target - num
            #check if complement in dict
            if complement in num_dict:
                return [num_dict[complement], i]
            #if yes return values

            #if no add current num to dict
            else:
                num_dict[num] = i