import java.util.Collection;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        //Count occurences
        Map<Integer, Integer> countMap = new HashMap<>();
        for(int num: arr){
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        //Obtain values
        Collection<Integer> counts = countMap.values();

        //Set of values
        Set<Integer> uniqueCounts = new HashSet<>(counts);
        //COmpare sizes
        return counts.size() == uniqueCounts.size();
    }
}