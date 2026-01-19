class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int duplicate = -1;
        int missing = -1;

        //Mark Visited with -
        for (int i = 0; i < n; i++){
            int val = Math.abs(nums[i]);
            if(nums[val - 1] < 0){
                duplicate = val;
            } else {
                nums[val - 1] *= -1;
            }
        }
        //Index that stays + is the one missing
        for (int i = 0; i< n; i++){
            if (nums[i] > 0){
                missing = i + 1;
            }
        }
        //return index
        return new int[]{duplicate, missing};
    }
}