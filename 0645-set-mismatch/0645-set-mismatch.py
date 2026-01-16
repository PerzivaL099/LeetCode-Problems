class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
       n = len(nums)
       expected_sum = n * (n+1) // 2
       actual_sum = sum(nums)

       #Eliminate duplicate
       unique_sum = sum(set(nums))

       #duplicate is difference between actual sum and sum withouth duplicates
       duplicate = actual_sum - unique_sum
       missing = expected_sum - unique_sum

       return [duplicate, missing]