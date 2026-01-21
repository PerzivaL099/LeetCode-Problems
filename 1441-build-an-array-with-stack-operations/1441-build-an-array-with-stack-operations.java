class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> Operations = new ArrayList<>();
        int current = 1;

        for (int num: target){
            while (current < num){
                Operations.add("Push");
                Operations.add("Pop");
                current++;
            }
            Operations.add("Push");
            current++;
        }

        return Operations;
    }
}