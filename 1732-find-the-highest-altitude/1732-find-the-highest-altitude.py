class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #Define values
        currentAltitude = 0
        maxAltitude = 0

        #Iterate through array
        for change in gain:
            #Update current altitude
            currentAltitude += change
                #Update
            maxAltitude = max(maxAltitude, currentAltitude)
        
        #return maxAltitude
        return maxAltitude
