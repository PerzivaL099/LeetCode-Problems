class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        #List to save operations
        Operations = []
        current = 1
        #Iterate through array
        for num in target:
            #If number is on target Push
            #if number not on target Push Pop
            while current < num:
                Operations.append("Push")
                Operations.append("Pop")
                current += 1

            Operations.append("Push")
            current += 1
        return Operations