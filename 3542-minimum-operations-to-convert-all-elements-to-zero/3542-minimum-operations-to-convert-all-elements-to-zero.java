class Solution {
    public int minOperations(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();

        int operations = 0;
        stack.push(0);

        for (int num: nums){
            while(!stack.isEmpty() && stack.peek() > num) {
                stack.pop();
            }
            if (stack.peek() < num){
                operations++;
                stack.push(num);
            }
        }
        return operations;
    }
}