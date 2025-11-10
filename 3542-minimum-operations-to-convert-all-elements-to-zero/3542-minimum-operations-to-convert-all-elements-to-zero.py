class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #counter of operations
        operations = 0
        stack = [0]
        #Iterate through array
        for num in nums:
            while num < stack[-1]:
                stack.pop()

            if num > stack[-1]:
                operations += 1
                stack.append(num)
        #return number of operations
        return operations

        