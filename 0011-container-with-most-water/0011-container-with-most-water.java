class Solution {
    public int maxArea(int[] height) {
        
        int left = 0;
        int right = height.length -1;
        int maxArea = 0;

        while(left < right){
            //Get current values 
            int currentHeight = Math.min(height[left], height[right]);
            int currentWidth = right - left;

            maxArea = Math.max(maxArea, currentHeight * currentWidth);
            
            // Move the shorter pointer inwards
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
      return maxArea;
    }
}