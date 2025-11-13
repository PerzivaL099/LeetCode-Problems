class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #New array and counters
        newArray = []

        #Iterate through array
        for i in range(n):
            #x values accesed normally
            xValues = nums[i]
            #y values start from n position forward
            yValues = nums[i + n]

            newArray.append(xValues)
            newArray.append(yValues)

        #If n=3 m[2,5,1] l[3,4,7] 
        return newArray

        