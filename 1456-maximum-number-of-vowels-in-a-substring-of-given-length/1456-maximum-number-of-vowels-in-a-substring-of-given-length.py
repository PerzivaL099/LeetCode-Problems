class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #Initialize which letters are vowels
        vowels = ['a','e','i','o','u']
        currentVowels = 0

        #Iterate through array
        
        for i in range(k):
            if s[i] in vowels:
                currentVowels += 1
        
        maxVowels = currentVowels

        for i in range(k, len(s)):
            charIn = s[i]       
            charOut = s[i - k]  
            
            if charIn in vowels:
                currentVowels += 1
            if charOut in vowels: 
                currentVowels -= 1

            # 3. Actualizar el máximo
            maxVowels = max(maxVowels, currentVowels)

        return maxVowels

    
        