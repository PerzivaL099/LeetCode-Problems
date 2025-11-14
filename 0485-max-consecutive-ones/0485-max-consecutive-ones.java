class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        //Array to store results
        int currentCount = 0;
        int maxCount = 0;
        //iterate throug array
        for(int i = 0;i < nums.length; i++){
            if(nums[i] == 1){
                currentCount++;
            } else if(nums[i] == 0){
                currentCount = 0;
            }
            
            if(currentCount > maxCount){
                maxCount = currentCount;
            }
            
        }
        return maxCount;
    }
}