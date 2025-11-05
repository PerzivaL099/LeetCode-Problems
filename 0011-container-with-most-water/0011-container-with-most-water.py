class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #Pointers
        pointer_l = 0
        pointer_r = len(height) - 1
        
        max_area = 0 
        
        while pointer_l < pointer_r: 
            
           #Get current values
            current_height = min(height[pointer_l], height[pointer_r])
            current_width = pointer_r - pointer_l
            
            
            current_area = current_height * current_width
            max_area = max(max_area, current_area)
                
           #Move pointers 
            if height[pointer_l] < height[pointer_r]:
                pointer_l += 1
            else:
                pointer_r -= 1
                
        
        return max_area