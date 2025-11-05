class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        #Pointers
        pointer_s = 0
        pointer_t = 0

        len_s = len(s)
        len_t = len(t)

            #Iterate through prime sequence
        while pointer_s < len_s and pointer_t < len_t:
                
                if s[pointer_s] == t[pointer_t]:
                #value of s and only pointer_t +1
                    pointer_s += 1
                #else both pointer +1
                pointer_t += 1
        #return boolean value 
        return pointer_s == len_s