class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #ResultArray
        resultArray = []
        
        #get values from array
        for number in nums:
            resultArray.append(number)
        
        for num in nums:
            resultArray.append(num)
        #return new array
        return resultArray
        