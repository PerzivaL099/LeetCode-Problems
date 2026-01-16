class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        //1.-clone array and sort it 
        int [] sortedNumbers = nums.clone();
        Arrays.sort(sortedNumbers);

        //2.-HaspMap to store(Number, SmallerNumber)
        Map<Integer, Integer> map = new HashMap<>();

        //3.-Fill Map
        for (int i = 0; i < sortedNumbers.length; i++){
            if (!map.containsKey(sortedNumbers[i])){
                map.put(sortedNumbers[i], i);
            }
        }
        //4.-Build new result
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            result[i] = map.get(nums[i]);
        }
        return result;
    }

}